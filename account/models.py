from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


def family_member_pic(instance,filename):
    return 'family_members/{}/{}'.format(instance.user.id,filename)


def profile_pic_path(instance,filename):
    return 'profile_pics/{}/{}'.format(instance.id,filename)


def profile_cover_pic_path(instance,filename):
    return 'profile_cover_pics/{}/{}'.format(instance.id,filename)


def delivery_partners_path(instance, filename):
    return 'delivery_partners/{}/{}'.format(instance.id,filename)

def vendor_invoices_path(instance, filename):
    return 'vendor_invoices/{}/{}'.format(instance.vendor.id,filename)

TYPE_OF_USERS = (
    ('member', 'Member'),
    ('business', 'Business'),
    ('ngo', 'Non Profitable Organization'),
    ('news_agency', 'News Agency')
)

class UserTypeCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name=_('Category Name'))
    name_es = models.CharField(max_length=50, null=True)
    name_fr = models.CharField(max_length=50, null=True)
    name_he = models.CharField(max_length=50, null=True)
    name_ru = models.CharField(max_length=50, null=True)
    name_ar = models.CharField(max_length=50, null=True)
    name_pt = models.CharField(max_length=50, null=True)
    name_de = models.CharField(max_length=50, null=True)
    user_type = models.CharField(max_length=20, choices=TYPE_OF_USERS)

    class Meta:
      verbose_name = "user_type_category"
      verbose_name_plural = "user_type_categories"


class Country(models.Model):
    name = models.CharField(max_length=80)
    numcode = models.SmallIntegerField()
    nicename = models.CharField(max_length=80)
    iso = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    phonecode = models.SmallIntegerField()


class Plan(models.Model):
    user_type = models.CharField(max_length=20, choices=TYPE_OF_USERS)
    name = models.CharField(max_length=10)
    amount = models.FloatField(validators=[MinValueValidator(0)])


PLAN_FEATURE_TYPE = (
    ("deal",_("Deal")),
    ("classified",_("Classified")),
    ("news",_("News")),
    ("job",_("Job")),
    ("location",_("Location")),
)

class PlanFeature(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    feature_type = models.CharField(max_length=20, choices=PLAN_FEATURE_TYPE, default="deal")
    numbers_allowed = models.IntegerField(default=0)


class ProductPrice(models.Model):
    product_name = models.CharField(max_length=100)
    cost = models.FloatField(validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class DeliveryPartner(models.Model):
    name = models.CharField(max_length=40,verbose_name=_('Name'))
    image = models.ImageField(max_length=256,null=True, upload_to=delivery_partners_path)
    created_at = models.DateTimeField(auto_now_add=True)


class MyUserManager(BaseUserManager):
    def create_user(self, email,user_type = None, phone=None, password=None):
        if not email:
            raise ValueError('Email is Required')

        user = self.model(
            email = email,
            # name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone=None, password=None):
        user = self.create_user(
            email=email,
            # name = name,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


LANGUAGES_ALLOWED = (
    ('en','English'),
    ('es','Spanish'),
    ('fr','French'),
    ('he','Hebrew'),
    ('ru','Russian'),
    ('de','German'),
    ('pt','Portuguese'),
    ('ar','Arabic'),
    
)


CURRENCIES_ALLOWED = (
    ('usd','Dollar'),
    ('eur','Euro'),
    ('gbp','British Pound'),
    ('ils','Israeli Shekels'),
    ('aud','Australian Dollar')
)


class Currency(models.Model):
    name = models.CharField(max_length=24)
    iso_code = models.CharField(max_length=3)
    sign = models.CharField(max_length=2,null=True)
    sign_svg = models.TextField(null=True)


class CurrencyExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='frm_cur')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_cur')
    rate_date = models.DateField()
    exchange_rate = models.DecimalField(decimal_places=2,max_digits=5)

    class Meta:
        unique_together = ('from_currency', 'to_currency','rate_date')


class BusinessCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name=_('Category Name'))
    name_es = models.CharField(max_length=50, null=True)
    name_fr = models.CharField(max_length=50, null=True)
    name_he = models.CharField(max_length=50, null=True)
    name_ru = models.CharField(max_length=50, null=True)
    name_ar = models.CharField(max_length=50, null=True)
    name_pt = models.CharField(max_length=50, null=True)
    name_de = models.CharField(max_length=50, null=True)
    keyword = models.CharField(max_length=50,verbose_name=_('Category Keyword'),null=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    display_type = models.CharField(max_length=20, default='dropdown')

    class Meta:
      verbose_name = "category"
      verbose_name_plural = "categories"



FAMILY_RELATIONS = (
    ('friend',_("Friends")),
    ('family',_("Family"))
)

USER_DELETE_REASONS = (
    ('expectation_not_meet', _("Didn't meet expectations")),
    ('handling_issue',  _("Too difficult to navigate, download, upload")),
    ("expensive", _("Too expensive")),
    ("choices_issue",  _("Not enough choices")),
    ("not_say",  _("Rather Not Say"))
)

SERVICE_PROVIDER_TYPES = (
    ('independent', 'Independent'),
    ('company', 'Company')
)

RESERVATION_WALKIN = (
    ('reservation','Need Reservation'),
    ('walkin','Walkin Allowed')
)

# Create your models here.
class MyUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True,verbose_name=_('Email Address'), max_length=220)
    phone = models.CharField(max_length=17,verbose_name=_('Phone Number'), null=True, blank=True)
    ngo = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='ngos_associated')
    user_type = models.CharField(max_length=20, choices=TYPE_OF_USERS)
    user_type_category = models.ForeignKey(UserTypeCategory, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=40, null=True, blank=True)
    lastname = models.CharField(max_length=40, null=True, blank=True)
    language = models.CharField(max_length=20, choices=LANGUAGES_ALLOWED,verbose_name=_('Language'), default="en")
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, related_name='user_currency', default=1, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(max_length=256,upload_to=profile_pic_path,verbose_name=_("Profile Pic"), default='default_images/default_profile_pic.jpeg')
    cover_pic = models.ImageField(max_length=256,upload_to=profile_cover_pic_path, verbose_name=_("Cover Picture"), default='default_images/default_cover_pic.png')
    
    paid_account = models.BooleanField(default=False,verbose_name=_("Paid Account"))
    parent = models.ForeignKey("self", null=True, related_name="family_member_user", on_delete=models.CASCADE)
    relation = models.CharField(max_length=10,choices=FAMILY_RELATIONS,verbose_name=_('Relation'), null=True)
    is_store = models.BooleanField(default=False)
    
    about = models.TextField(blank=True, null=True,verbose_name=_("About"))
    name = models.CharField(max_length=100,verbose_name=_('Name'), null=True, blank=True)
    administrator_name = models.CharField(max_length=100,verbose_name=_('Administrator Name'), null=True, blank=True)
    business_category = models.ForeignKey(BusinessCategory,verbose_name=_("Business Category"), null=True, blank=True, on_delete=models.SET_NULL)
    business_contact = models.CharField(max_length=11, blank=True, null=True,verbose_name=_("Business Contact"))
    business_email = models.EmailField(max_length=220, blank=True, null=True,verbose_name=_("Business Email"))
    website_url = models.TextField(blank=True, null=True,verbose_name=_("Website Url"))
    facebook_url = models.TextField(blank=True, null=True,verbose_name=_("Facebook"))
    twitter_url = models.TextField(blank=True, null=True,verbose_name=_("Twitter"))
    instagram_url = models.TextField(blank=True, null=True,verbose_name=_("Instagram"))
    youtube_url = models.TextField(blank=True, null=True,verbose_name=_("Youtube"))
    
    favourite_user = models.ManyToManyField("self", default=None, blank=True, symmetrical=False, related_name="favourite_users") #symmetrical=False ignores cyclic object store
    favourite_deal = models.ManyToManyField("deals.Deal", default=None, blank=True, symmetrical=False, related_name="favourite_deals") #symmetrical=False ignores cyclic object store
    favourite_classified = models.ManyToManyField("classifieds.Classified", default=None, blank=True, symmetrical=False, related_name="favourite_classifieds") #symmetrical=False ignores cyclic object store
    favourite_ngo_video = models.ManyToManyField("account.NgoVideo", default=None, blank=True, symmetrical=False, related_name="favourite_ngo_videos") #symmetrical=False ignores cyclic object store
    favourite_job = models.ManyToManyField("jobs.Job", default=None, blank=True, symmetrical=False, related_name="favourite_jobs") #symmetrical=False ignores cyclic object store

    newsletter_subscribed = models.BooleanField(default=False,verbose_name=_('Newsletter Subscribed'))
    
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    plan_upgrade_date = models.DateField(null=True)
    delivery_partner = models.ManyToManyField(DeliveryPartner, default=None, blank=True)
    service_provider_type = models.CharField(max_length=16, choices=SERVICE_PROVIDER_TYPES, null=True)
    reservation_walkin = models.CharField(max_length=16, choices=RESERVATION_WALKIN, null=True)

    stripe_customer_id = models.CharField(null=True, max_length=100)
    
    is_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    delete_reason = models.CharField(null=True, choices=USER_DELETE_REASONS, max_length=50)
    is_default_ngo = models.BooleanField(default=False)

    extra_deal = models.BooleanField(default=False)
    extra_weekly_deal = models.BooleanField(default=False)
    extra_classified = models.BooleanField(default=False)
    extra_location = models.IntegerField(default=0)

    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def get_full_name(self):

        try:
            user_email = self.email.replace('-', '')
            uuid.UUID(str(user_email))
            return "DELETED USER"
        except ValueError:
            pass

        if self.is_deleted:
            return "DELETED USER"


        fullname = ''

        if self.firstname and self.lastname:
            return self.firstname+" "+self.lastname
        
        if self.firstname:
            fullname += self.firstname
        if self.lastname:
            fullname += self.lastname

        if not fullname:
            fullname = self.name

        return fullname
    
    
    def get_primary_location(self):
        
        try:
            primary_location = UserLocation.objects.get(user = self, is_primary = True)
        except:
            return ""

        if primary_location:
            loc = primary_location.location
            full_location = ""
            if loc.location:
                full_location += loc.location + " "
            if loc.address:
                full_location += loc.address + " "
            if loc.city:
                full_location += loc.city + " "
            if loc.state:
                full_location += loc.state + " "
            if loc.country:
                full_location += loc.country + " "
            if loc.zipcode:
                full_location += loc.zipcode

            return full_location
        
    def get_ngo_total_amount(self):
        payouts = NGOPayout.objects.filter(ngo=self).aggregate(Sum('amount'))
        return payouts['amount__sum']
    
    def get_ngo_paid_amount(self):
        payouts = NGOPayout.objects.filter(ngo=self,payout=1).aggregate(Sum('amount'))
        paid_payouts = payouts['amount__sum']
        if not paid_payouts:
            paid_payouts = 0
        return paid_payouts
    
    def get_ngo_outstanding_amount(self):
        total_payouts = NGOPayout.objects.filter(ngo=self).aggregate(Sum('amount'))
        total_payouts = total_payouts['amount__sum']

        paid_payouts = NGOPayout.objects.filter(ngo=self,payout=1).aggregate(Sum('amount'))
        paid_payouts = paid_payouts['amount__sum']
        if not paid_payouts:
            paid_payouts = 0

        return total_payouts - paid_payouts


        

PAYMENT_ITEMS = (
    ('plan', 'Plan'),
    ('deal', 'Deal'),
    ('weekly_deal','Weekly Deal'),
    ('location','Location'),
    ('classified','Classified'),
    ('new_payment_method','New Payment Method')
)

PAYMENT_STATUS = (
    ('pending',_('Pending')),
    ('complete',_('Complete')),
    ('cancelled',_('Cancelled')),
)

PAYMENT_GATEWAYS = (
    ('stripe','Stripe'),
    ('tranzila','Tranzila'),
)

class PaymentDetail(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name="temp_payment_detail", null=True)
    item_type = models.CharField(max_length=20, choices=PAYMENT_ITEMS, default="plan")
    plan_to_activate = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    locations_to_activate = models.IntegerField(default=0)
    main_amount_in_usd = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=10, null=True)
    status = models.CharField(choices=PAYMENT_STATUS, max_length=20, default="pending")
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class StripeDetailNew(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name="stripe_detail_new", null=True)
    payment_detail = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, related_name="stripe_payment_detail", null=True)
    intent = models.CharField(max_length=200)
    event_type = models.CharField(null=True, max_length=100)
    payment_method = models.TextField(null=True)
    card_mask = models.CharField(max_length=30, null=True)
    expire_month = models.CharField(max_length=4, null=True)
    expire_year = models.CharField(max_length=4, null=True)
    amount = models.FloatField(default=0.0)
    currency = models.CharField(max_length=10, null=True)
    status = models.CharField(choices=PAYMENT_STATUS, max_length=20, default="pending")
    cancellation_reason = models.TextField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class StripePaymentMethod(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name="stripe_payment_methods", null=True)
    payment_method = models.TextField(null=True)
    card_mask = models.CharField(max_length=30, null=True)
    expire_month = models.CharField(max_length=4, null=True)
    expire_year = models.CharField(max_length=4, null=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TranzilaDetail(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name="tranzila_detail", null=True)
    payment_detail = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, related_name="tranzila_payment_detail", null=True)
    message = models.TextField()
    processor_response_code = models.IntegerField(null=True)
    transaction_id = models.IntegerField(null=True)
    currency_code = models.CharField(max_length=2, null=True)
    expiry_month = models.CharField(max_length=4, null=True)
    expiry_year = models.CharField(max_length=4, null=True)
    payment_plan = models.CharField(max_length=4, null=True)
    credit_card_owner_id = models.CharField(max_length=100, null=True)
    token = models.CharField(max_length=100, null=True)
    card_last_four = models.CharField(max_length=4, null=True)
    card_mask = models.CharField(max_length=30, null=True)
    card_locality = models.CharField(max_length=20, null=True)
    amount = models.FloatField(default=0)
    txn_type = models.CharField(max_length=10, null=True)
    tranmode = models.CharField(max_length=10, null=True)
    status = models.CharField(choices=PAYMENT_STATUS, max_length=20, default="pending")
    error_code = models.CharField(max_length=10, null=True)
    error_info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class TranzilaToken(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='tranzila_tokens')
    token = models.CharField(max_length=100)
    card_mask = models.CharField(max_length=30, null=True)
    expire_month = models.CharField(max_length=4)
    expire_year = models.CharField(max_length=4)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TempToken(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, related_name='temp_token')
    token = models.CharField(max_length=100, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} - {}'.format(self.user.phone, self.token)
    

class NgoReferalToken(models.Model):
    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, related_name='ngo_referal')
    referal_token = models.CharField(max_length=100, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


CODE_CHOICES = (
    ('Register', 'Register'),
    ('Forgot', 'Forgot'),
    ('Change Email','Change Email')
)

class Code(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=6)
    usage = models.CharField(max_length=20, choices=CODE_CHOICES, default='Register')
    created_at = models.DateTimeField(auto_now=True)


class FamilyMember(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="family_member")
    fullname = models.CharField(max_length=50, verbose_name=_("Full Name"))
    relation = models.CharField(max_length=10,choices=FAMILY_RELATIONS,verbose_name=_('Relation'))
    image = models.ImageField(max_length=256,upload_to=family_member_pic,verbose_name=_('Member Pic'), default='default_images/default_profile_pic.jpeg')
    email_add = models.EmailField(verbose_name=_('Email Address'), max_length=220)
    phone_num = models.CharField(max_length=17,verbose_name=_('Phone Number'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "default_images/default_profile_pic.jpeg"


class RestaurantMenu(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='restaurant_menu')
    menu = models.FileField(verbose_name=_("Menu"))
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='reviews')
    reviewed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_reviewers')
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewMark(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='marked_by_user')
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='marked_review')
    mark_type = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewFlag(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='flaggers')
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='flagged_reviews')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class NgoVideo(models.Model):
    user = models.ForeignKey(MyUser, related_name='ngo_videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=_('Video Title'))
    link = models.URLField(verbose_name=_('Video Link'))
    # users_liked = models.ManyToManyField(MyUser, related_name='users_liked',blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
   store_manager_email = models.EmailField(max_length=256,verbose_name=_('Store Managed Email Address'), null=True)
   store_manager_phone = models.CharField(max_length=17,verbose_name=_('Store Managed Phone Number'), null=True)
   location = models.TextField(blank=True, null=True,verbose_name=_("Location Name"))
   latitude = models.DecimalField(max_digits=10, decimal_places=5, validators=[MinValueValidator(-90), MaxValueValidator(90)])
   longitude = models.DecimalField(max_digits=10, decimal_places=5, validators=[MinValueValidator(-180), MaxValueValidator(180)])
   address = models.TextField(verbose_name=_("Address"), default='')
   city = models.CharField(max_length=30,verbose_name=_("City"))
   state = models.CharField(max_length=30,verbose_name=_("State"))
   country = models.CharField(max_length=20,verbose_name=_("Country"))
   zipcode = models.CharField(verbose_name=_("Zipcode"), max_length=12)
   created_at = models.DateTimeField(auto_now_add=True)

   def get_location_detail(self):
        
        detail = []
        detail.append(self.location)
        detail.append(self.address)
        detail.append(", "+self.city)
        detail.append(self.state)
        detail.append(self.country)
        detail.append(", "+self.zipcode)

        detail = " ".join(detail)
        
        return detail


class UserLocation(models.Model):
   user = models.ForeignKey(MyUser, related_name='user_locations', on_delete=models.SET_NULL, null=True)
   location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
   is_primary = models.BooleanField(default=False)



class Flagged(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='flags')
    flagged_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_flaggers')
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


ACTIVITY_TYPE = (
    ('login', 'Login'),
    ('logout', 'Logout')
)

class ActivityLog(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    type = models.CharField(max_length=10, default='login', choices=ACTIVITY_TYPE)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)


class NGOPayout(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name="paying_users")
    payment_detail = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, related_name="ngo_payment_detail", null=True)
    ngo = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name="paid_ngos")
    amount = models.FloatField()
    payout = models.BooleanField(default=False)
    payout_date = models.DateTimeField(null=True)
    paid_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name="updated_by")
    created_at = models.DateTimeField(auto_now_add=True)


class Revenue(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, related_name="revenue_paying_users")
    payment_detail = models.ForeignKey(PaymentDetail, on_delete=models.SET_NULL, related_name="revenue_payment_detail", null=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name


class VendorExpense(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    invoice_number = models.CharField(max_length=100)
    file = models.FileField(upload_to=vendor_invoices_path)
    amount = models.FloatField(default=0.0)
    date = models.DateField(null=True)
    remarks = models.TextField(null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class OnelineUser(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='online_user')
    created_at = models.DateTimeField(auto_now_add=True)