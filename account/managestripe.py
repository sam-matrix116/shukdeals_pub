import stripe
import json
from django.conf import settings
from account.models import StripePaymentMethod

stripe.api_key = settings.STRIPE_API_KEY


def get_stripe_customer_id(user):
    
    user_stripe_customer_id = user.stripe_customer_id
    
    if not user_stripe_customer_id:
        
        cust_resp = stripe.Customer.create(
            email = user.email,
            phone = user.phone,
            name = user.firstname,
            description="Customer:{}, ID: {}".format(user.firstname,user.id),
        )
        user_stripe_customer_id = cust_resp.id
        user.stripe_customer_id = user_stripe_customer_id
        user.save()

    return user_stripe_customer_id


def stripe_payment_intent(user,amount):
    
    resp = stripe.PaymentIntent.create(
            customer = get_stripe_customer_id(user),
            amount = int(amount*100),
            currency = user.currency.iso_code,
            automatic_payment_methods = {"enabled": True},
            setup_future_usage = "off_session",
            description="Customer:{}, ID: {}".format(user.firstname,user.id),
        )
    
    # print(resp)

    return resp


def stripe_payment_offsession(user,amount,payment_method):

    try:
        resp = stripe.PaymentIntent.create(
                customer=user.stripe_customer_id,
                payment_method = payment_method,
                amount = int(amount*100),
                currency = user.currency.iso_code,
                off_session = True,
                description="Customer:{}, ID: {}".format(user.firstname,user.id),
                confirm=True
            )
    except:
        return ""
    
    # print(resp)

    return resp


def get_stripe_payment_methods(user):

    
    stripe.api_key = settings.STRIPE_API_KEY

    resp = stripe.Customer.list_payment_methods(
        get_stripe_customer_id(user),
        limit=5,
    )
    return resp


def create_checkout_session(user):
    
    resp = stripe.checkout.Session.create(
        mode="setup",
        currency="usd",
        customer=get_stripe_customer_id(user),
        success_url= settings.FRONTEND_URL+"success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url= settings.FRONTEND_URL+"cancel",
        )

    return resp


def retrieve_checkout_session(user, CHECKOUT_SESSION_ID):

    customer_id = get_stripe_customer_id(user)
    
    resp = stripe.checkout.Session.retrieve(CHECKOUT_SESSION_ID,)
    setup_intent = resp.setup_intent
    
    resp = stripe.SetupIntent.retrieve(setup_intent)
    print("resp",resp)
    payment_method = resp.payment_method

    stripe.PaymentMethod.attach(payment_method, customer=customer_id,)

    # add payment method to db
    payment_method_obj = stripe.Customer.retrieve_payment_method(
        customer_id,
        payment_method,
    )

    try:
        StripePaymentMethod.objects.get(payment_method=payment_method)
    except:
        new_stripe_pm = StripePaymentMethod.objects.create(
            user = user,
            payment_method = payment_method,
            card_mask = payment_method_obj.card.last4,
            expire_month = payment_method_obj.card.exp_month,
            expire_year = payment_method_obj.card.exp_year,
        )

        if StripePaymentMethod.objects.filter(user=user).count() == 1:
            new_stripe_pm.is_default = True
            new_stripe_pm.save()


def detach_payment_method(payment_method):

    stripe.PaymentMethod.detach(payment_method)
