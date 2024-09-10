from django.core.management.base import BaseCommand, CommandError
from account.models import MyUser, TranzilaDetail, StripeDetailNew
from account.utils import convert_currency as __, create_plan_payment, handle_payment_intent_succeeded_new
from account.managetranzila import *
from account.managestripe import stripe_payment_offsession
import requests

import logging
logger = logging.getLogger('demo_log')
logger = logging.getLogger('django')


class Command(BaseCommand):
    help = "Run this command on first day of every month"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        
        plan_users = MyUser.objects.filter(plan__amount__gt = 0, is_deleted = False)
        
        for user in plan_users:

            # if user.id != 19:
            #     continue

            print("Handling Billing Cycle for: Customer:{}, ID: {}".format(user.firstname,user.id))
            
            payment_detail = create_plan_payment(user.plan, user)
            
            if not payment_detail:
                continue

            if user.currency.iso_code == 'ils':

                last_valid_transaction = TranzilaDetail.objects.filter(user=user, status='complete').last()
                if last_valid_transaction:
                    tranzila_token = last_valid_transaction.token

                    try:
                        tranzila_token = TranzilaToken.objects.get(token=tranzila_token, user=user)
                    except:
                        tranzila_token  = None

                    if tranzila_token:

                        payment_status = process_tranzila_payment(tranzila_token,payment_detail)
                        if payment_status['code'] == 1:
                            handle_payment_intent_succeeded_new(payment_detail)
                            logger.info("....tranzila success....")
                        else:
                            logger.info("....process tranzila failed for user:{}....".format(user.id))
                    else:
                        logger.info("....Tranzila token not found for user:{}....".format(user.id))
                else:
                    logger.info("....tranzila failed. No last transaction found....")

            else:
                
                stripe_detail = StripeDetailNew.objects.filter(user=user, status='complete').last()
                if stripe_detail:
                    payment_method=stripe_detail.payment_method

                    resp = stripe_payment_offsession(user=user,amount=10,payment_method=payment_method)

                    if not resp:
                        payment_detail.status = "cancelled"
                        payment_detail.save()
                        logger.info("....stripe failed....")
                        continue

                    charges_detail = resp["charges"]["data"][0]

                    if charges_detail["paid"]:

                        StripeDetailNew.objects.create(
                            user = user,
                            payment_detail = payment_detail,
                            intent = charges_detail["payment_intent"],
                            payment_method = charges_detail["payment_method"],
                            amount = charges_detail["amount"],
                            currency = charges_detail["currency"],
                            status = "complete",
                            description = charges_detail["description"]
                        )

                        payment_detail.status = 'complete'
                        payment_detail.save()

                        handle_payment_intent_succeeded_new(payment_detail)
                        logger.info("....stripe success....")

                    else:

                        
                        payment_detail.status = "cancelled"
                        payment_detail.save()
                        logger.info("....stripe failed....")

                else:

                    payment_detail.status = "cancelled"
                    payment_detail.save()
                    logger.info("....stripe failed....")


            
        self.stdout.write(
            self.style.SUCCESS('Monthly cycle run successfully')
        )