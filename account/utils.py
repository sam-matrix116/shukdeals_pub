from email.policy import default
from django.conf import settings
from random import randint
from django.core.mail import EmailMultiAlternatives
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import get_language, activate, gettext
import re
from account.models import TempToken, MyUser, Plan, CurrencyExchangeRate, PlanFeature, Currency, Location, PaymentDetail, NGOPayout, Revenue, ProductPrice
from deals.models import Deal
from classifieds.models import Classified
import os
from twilio.rest import Client
from datetime import date
import uuid
import random
from django.db.models.functions import Concat
from django.db.models import Value, Q

import logging
logger = logging.getLogger('demo_log')
logger = logging.getLogger('django')



def active_users():
    users = MyUser.objects.filter(is_verified = True, is_admin=False, is_superuser=False, is_staff=False, active=True, is_deleted = False).annotate(fullname=Concat('firstname', Value(' '), 'lastname'))
    return users


def active_ngos():
    users = MyUser.objects.filter(is_admin=False, is_superuser=False, is_staff=False, active=True, is_deleted = False).annotate(fullname=Concat('firstname', Value(' '), 'lastname'))
    return users


def active_businesses():
    users = MyUser.objects.filter(is_verified = True, is_admin=False, is_superuser=False, is_staff=False, active=True, is_deleted = False, is_approved=True)
    return users




def translate(text):
    # activate(language)
    text = gettext(text)
    return text


def get_random_code():
    number = randint(111111,999999)
    return str(number)


def send_email(to_email, subject, text_content, html_content):
    print("--sending email start---")
    if settings.EMAIL_ON:
        from_email, to = settings.EMAIL_FROM_EMAIL, to_email
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        status = msg.send()
        return status    
    print("--sending email end---")


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def get_map_for_language(lang):
    if lang == 'en':
        img = 'as'
    elif lang == 'he':
        img = 'il'
    else:
        img = lang.lower()

    return '/static/flags/'+img+".png"


def get_map_for_currency(curr):
    if curr == 'usd':
        img = 'as'
    elif curr == 'eur':
        img = 'de'
    elif curr == 'gbp':
        img = 'gb'
    elif curr == 'ils':
        img = 'il'
    elif curr == 'aud':
        img = 'au'
    else:
        img = curr.lower()

    return '/static/flags/'+img+".png"


def is_valid_email(s):
   pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   if re.match(pat,s):
      return True
   return False


def is_valid_phone(p):
   length = len(p)
   p = p[length-10:]
   if p.isnumeric():
       return True

   return False

def reload_token(user):
    TempToken.objects.filter(user=user).delete()
    temp_code = TempToken(user=user)
    temp_code.save()
    return temp_code.token


def get_valid_other_user(request,user_id):
    print("request.user.id",request.user.id)
    print("user_id",user_id)
    if request.user.id == user_id:
        return False
    
    try:
        user = MyUser.objects.get(id=user_id, is_verified = True, is_admin=False, is_superuser=False, is_staff=False)
    except:
        return False
    
    return user


def get_default_plan(user):

    try:
        plan_to_activate = Plan.objects.get(user_type = user.user_type, amount=0)
    except:
        return None
    
    return plan_to_activate


def convert_currency(amount, from_currency, to_currency):

    if not from_currency or not to_currency or not amount:
        return amount
    

    # print("Converting currency amount:{} from:{}, to:{}".format(amount, from_currency, to_currency))

    curr_exch = None

    try:
        from_currency = Currency.objects.get(iso_code = from_currency)
    except:
        from_currency = None

    
    try:
        to_currency = Currency.objects.get(iso_code = to_currency)
    except:
        to_currency = None

    if from_currency and to_currency:
        try:
            curr_exch = CurrencyExchangeRate.objects.get(from_currency = from_currency, to_currency = to_currency)
        except:
            print("Currency exchange not found")
            pass
    if curr_exch:
        return round(float(amount) * float(curr_exch.exchange_rate),2)
    
    return amount


def check_plan_exceeded(user,type):

    try:
        plan_feature = PlanFeature.objects.get(feature_type = type, plan = user.plan)
    except:
        print("Plan feature for feature_type:{} and plan_id:{} not found".format(type, user.plan.id))
        return True

    if type == 'deal':
        already_created_deals = Deal.objects.filter(user=user).count()
        if already_created_deals >= plan_feature.numbers_allowed:
            return True
        
    
    if type == 'classified':
        already_created_classifieds = Classified.objects.filter(user=user).count()
        if already_created_classifieds >= plan_feature.numbers_allowed:
            return True
    
    
    return False


def exchange_rate(from_curr, to_curr):

    import requests

    url = "https://xecdapi.xe.com/v1/convert_to?from="+to_curr+"&to="+from_curr+"&amount=1"

    payload = {}
    headers = {
    'accept': 'application/json',
    'Authorization': 'Basic ZGlnbml0ZWNobWVkaWF3b3Jrc3B2dGx0ZDcyOTMwMjg5NTptMjFtbHZ1cnM4M3VwNzdtdjMzMTUwNXFpdA=='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def random_string(len=10):
    import random, string
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(len))
    return x


def send_otp_on_phone(number):
    # Download the helper library from https://www.twilio.com/docs/python/install
    
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    verify_sid = settings.TWILIO_VERIFY_SID
    verified_number = number

    client = Client(account_sid, auth_token)

    try:
        verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=verified_number, channel="sms")
        status = verification.status
    except:
        status = 'error'
    
    return status


def verify_otp_on_phone(number,otp):
    # Download the helper library from https://www.twilio.com/docs/python/install
    

    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    verify_sid = settings.TWILIO_VERIFY_SID
    verified_number = number

    client = Client(account_sid, auth_token)

    try:
        verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp)
        status = verification_check.status
        
    except:
        status = 'error'

    print('status',status)
    return status


def get_single_product_cost(user,module,deal_type,return_type,items_count=None):

    main_amount_in_usd = 0
    shuk_fee = 0

    if module == 'deal':
        product_price = ProductPrice.objects.get(product_name = 'SINGLE_DEAL_COST')
        
        if deal_type == 'weekly':
            product_price = ProductPrice.objects.get(product_name = 'SINGLE_WEEKLY_DEAL_COST')
            
            if user.user_type == 'business' and user.plan and user.plan.amount == 0:
                product_price = ProductPrice.objects.get(product_name = 'FREE_BUSINESS_SINGLE_WEEKLY_DEAL_COST')

    elif module == 'classified':
        
        product_price = ProductPrice.objects.get(product_name = 'FREE_MEMBER_SINGLE_CLASSIFIED_COST')

    main_amount_in_usd = float(product_price.cost)

    if return_type == 'main_amount':
        return main_amount_in_usd

    else:

        shuk_fee = main_amount_in_usd * settings.SHUK_PERCENTAGE / 100

        return shuk_fee
    
def convert_to_int(val):
    if val:
        return int(val)
    else:
        return 0
    


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def create_plan_payment(plan, user):

    currency = 'usd'
    amount = plan.amount
    main_amount_in_usd = plan.amount
    if user.currency.iso_code != 'usd':
        currency = user.currency.iso_code
        amount = convert_currency(amount, 'usd', currency)

    # check what was user's last plan upgrade date
    plan_upgrade_date = user.plan_upgrade_date
    print("plan_upgrade_date",plan_upgrade_date)
    if plan_upgrade_date:
        days_not_used = int(plan_upgrade_date.strftime("%d"))
        if days_not_used == 31:
            days_not_used = 30
        print("days_not_used",days_not_used)
        plan_per_day_cost = plan.amount/30
        print("plan_per_day_cost",plan_per_day_cost)
        amount_to_deduct = days_not_used * plan_per_day_cost
        print("amount_to_deduct",amount_to_deduct)
        main_amount_in_usd = plan.amount - amount_to_deduct
        print("main_amount_in_usd",main_amount_in_usd)
        amount = convert_currency(main_amount_in_usd, 'usd', currency)
        print("amount",amount)

    # the last payment was done on 30 or 31, so no monthly billing should be deducted
    if amount == 0:
        return False
    
    payment_detail = PaymentDetail.objects.create(
        user = user,
        plan_to_activate = plan,
        main_amount_in_usd = main_amount_in_usd,
        amount = amount,
        currency = currency
    )

    return payment_detail


def handle_payment_intent_succeeded_new(payment_detail):

    # if the transaction is for deal, allow deals additions
    logger.info("handle_payment_intent_succeeded_new_started")
    if payment_detail.status == "complete":

        logger.info("payment_detail.status == complete")

        logger.info("payment_detail.item_type")
        logger.info(payment_detail.item_type)

        if payment_detail.item_type == "plan":
            payment_detail.user.plan = payment_detail.plan_to_activate
            payment_detail.user.plan_upgrade_date = date.today()
            payment_detail.user.save()

            try:
                location_plan_feature = PlanFeature.objects.get(plan = payment_detail.plan_to_activate, feature_type = 'location')
            except:
                location_plan_feature = None
            
            if location_plan_feature and location_plan_feature.numbers_allowed > 0:
                payment_detail.user.extra_location += location_plan_feature.numbers_allowed
                payment_detail.user.save()

        payment_detail.user.paid_account = True
        payment_detail.user.save()

        if payment_detail.item_type == "deal":
            payment_detail.user.extra_deal = True
            payment_detail.user.save()

        if payment_detail.item_type == "weekly_deal":
            payment_detail.user.extra_weekly_deal = True
            payment_detail.user.save()

        if payment_detail.item_type == "classified":
            payment_detail.user.extra_classified = True
            payment_detail.user.save()

        # if the transaction is for locations, allow deals additions
        if payment_detail.item_type == "location":
            payment_detail.user.extra_location += payment_detail.locations_to_activate
            payment_detail.user.save()

        # add NGO PAYOUT
        ngo_amount = 0
        shuk_amount = 0
        if payment_detail.item_type == 'location':
            main_amount = payment_detail.main_amount_in_usd / payment_detail.locations_to_activate
        else:
            main_amount = payment_detail.main_amount_in_usd
        
        shuk_amount = (main_amount * settings.SHUK_PERCENTAGE / 100)
        ngo_amount = (main_amount * settings.NGO_PERCENTAGE / 100)

        if payment_detail.item_type == 'location' and payment_detail.locations_to_activate > 0:
            ngo_amount = ngo_amount * payment_detail.locations_to_activate
            shuk_amount = shuk_amount * payment_detail.locations_to_activate

        shuk_amount = round_off(shuk_amount)
        ngo_amount = round_off(ngo_amount)

        logger.info("Creating ngo payout with amount: {}".format(ngo_amount))
        NGOPayout.objects.create(
            user = payment_detail.user,
            payment_detail = payment_detail,
            ngo = payment_detail.user.ngo,
            amount = ngo_amount
        )

        logger.info("Creating revenue with amount: {}".format(shuk_amount))
        Revenue.objects.create(
            user = payment_detail.user,
            payment_detail = payment_detail,
            amount = shuk_amount
        )
    
    else:
        logger.info("payment_detail.status == failed")

def round_off(amount):
    return round(amount, 0)


def randomise_string():
    return uuid.uuid4()

def randomise_string_short():
    return str(uuid.uuid4())[:8]

def get_random_phone():
    import time
    return int(time.time())


def randomize_all_user_data(user):
    # randomize user email
    user.email = randomise_string()
    user.phone = get_random_phone()
    user.firstname = randomise_string()
    user.lastname = randomise_string()
    user.about = None
    user.name = None
    user.administrator_name = None
    user.business_contact = None
    user.business_email = None
    user.website_url = None
    user.facebook_url = None
    user.twitter_url = None
    user.instagram_url = None
    user.youtube_url = None
    user.country = None
    user.currency = None
    user.stripe_customer_id = None

    image = user.image
    if image:
        image = image.url.strip("/")
        file = os.path.join(settings.BASE_DIR,image)
        if os.path.isfile(file):
            os.remove(file)
        user.image = None

    cover_pic = user.cover_pic
    if cover_pic:
        cover_pic = cover_pic.url.strip("/")
        file = os.path.join(settings.BASE_DIR,cover_pic)
        if os.path.isfile(file):
            os.remove(file)
        user.cover_pic = None
    
    
    user.save()


def allocate_members_and_businesses_to_default_ngo(user):
    
    try:
        default_ngo = active_ngos().get(is_default_ngo = True)
    except:
        return False
    
    logger.info("Allocating members and busineses to default ngo:"+default_ngo.name)

    members_and_businesses = MyUser.objects.filter(is_deleted=False,ngo=user).filter(Q(user_type='member')|Q(user_type='business'))

    custom_message = "The Non Profitable Organization associated with your account: {} has deleted its account. Your account has been allocated to another Non Profitable Account: {}".format(user.name, default_ngo.name)

    subject = '[Shuk.tv] Non Profitable Organization Updated'
    plaintext = get_template('emails/user-email.txt')
    htmly     = get_template('emails/user-email.html')
    d = {'custom_message': custom_message}
    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    for user in members_and_businesses:
        print("sending email to emai id:"+user.email)
        try:
            status = send_email(user.email, subject, text_content, html_content)
        except:
            status = False

    members_and_businesses.update(ngo = default_ngo)

    return True