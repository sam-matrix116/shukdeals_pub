from django.conf import settings
import requests
import json
from account.models import TranzilaDetail, TranzilaToken
from account.utils import convert_currency as __
from django.utils.translation import gettext as _


def tranzila_token_exist(user):

    user_tranzila_token = hasattr(user, 'tranzila_token')

    if not user_tranzila_token:
        return False

    return user_tranzila_token


def process_tranzila_payment(tranzila_token,payment_detail,card_number=None,expire_month=None,expire_year=None):
    
    if tranzila_token:
        card_number = tranzila_token.token
        expire_month = int(tranzila_token.expire_month)
        expire_year = int(tranzila_token.expire_year)
    
        
        
    unit_price =  payment_detail.amount

    url = settings.TRANZILA_TRANSACTION_CREATE_URL

    payload = json.dumps({
      "terminal_name": "shukdeals",
      "txn_currency_code": "ILS",
      "txn_type": 'debit',  
      "reference_txn_id" : 298, 
      "authorization_number" : "0971703",
      "card_number" : card_number,
      "expire_month" : expire_month, 
      "expire_year": expire_year,
      "payment_plan": 1,  
      "items": [
        {
          "code": "1",
          "name": payment_detail.item_type+" :: payment detail id:"+str(payment_detail.id),
          "unit_price": unit_price,      
          "type": "I",
          "units_number": 1,
          "unit_type": 1,
          "price_type": "G",
          "currency_code": "ILS",
          "to_txn_currency_exchange_rate": 1,
          "attributes": [
            {
              "language": "hebrew",
              "name": "attribute name",
              "value": "attribute value"
            }
          ]
        }
      ],
      "response_language": "english",
      "user_defined_fields": [
        {
          "name": "company",
          "value": "test 222"
        }
      ] 
    })

    # print("payload",payload)


    import hmac
    import hashlib
    import time
    import binascii
    import secrets
    timestamp = str(int(time.time()))
    
    app_key = settings.TRANZILA_APP_KEY
    secret = settings.TRANZILA_SECRET
    nonce = str(binascii.hexlify(secrets.token_bytes(40)), 'utf-8')
    access_key = hmac.new(bytes(secret + str(timestamp) + nonce, 'utf-8'), bytes(app_key, 'utf-8'), hashlib.sha256).hexdigest()

    headers = {
    'X-tranzila-api-app-key': app_key,
    'X-tranzila-api-request-time': timestamp,
    'X-tranzila-api-nonce': nonce,
    'X-tranzila-api-access-token': access_key,
    'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

    # print('response',response.text)

    resp = json.loads(response.text)

    # print("resp",json.dumps(resp, indent=4))
    payment_method_message = ''
    if "error_code" in resp and resp["error_code"] == 0:
        # transaction is successful
        transaction_result = resp["transaction_result"]
        TranzilaDetail.objects.create(
            user = payment_detail.user,
            payment_detail = payment_detail,
            message = resp["message"],
            processor_response_code = transaction_result["processor_response_code"],
            transaction_id = transaction_result["transaction_id"],
            currency_code = transaction_result["currency_code"],
            expiry_month = transaction_result["expiry_month"],
            expiry_year = transaction_result["expiry_year"],
            payment_plan = transaction_result["payment_plan"],
            credit_card_owner_id = transaction_result["credit_card_owner_id"],
            token = transaction_result["token"],
            card_last_four = transaction_result["last_4"],
            card_mask = transaction_result["card_mask"],
            card_locality = transaction_result["card_locality"],
            amount = transaction_result["amount"],
            txn_type = transaction_result["txn_type"],
            tranmode = transaction_result["tranmode"],
            status = 'complete'
        )

        try:
          TranzilaToken.objects.get(token=transaction_result["token"])
          payment_method_message = "This payment method already exist."
        except:
            new_tranzila_pm = TranzilaToken.objects.create(
                user = payment_detail.user,
                token = transaction_result["token"],
                expire_month = transaction_result["expiry_month"],
                expire_year = transaction_result["expiry_year"],
                card_mask = transaction_result["card_mask"],
            )
            payment_method_message = "New payment method added successfully."

            if TranzilaToken.objects.filter(user=payment_detail.user).count() == 1:
                new_tranzila_pm.is_default = True
                new_tranzila_pm.save()

        code = 1
        message = _("Transaction successful")

        payment_detail.status = 'complete'
        payment_detail.save()
    
    else:
        
        TranzilaDetail.objects.create(
            user = payment_detail.user,
            payment_detail = payment_detail,
            error_code = resp["error_code"] if "error_code" in resp else resp["code"],
            error_info = resp["mismatch_info"] if "mismatch_info" in resp else "",
            message = resp["message"],
            status = 'cancelled'
        )

        code = 0
        message = resp["message"]
        payment_method_message = "Some problem in adding the new payment method."

        payment_detail.status = 'cancelled'
        payment_detail.save()
      
    resp = {
        "code": code,
        "message": message,
        "payment_method_message":payment_method_message,
        "payment_detail": payment_detail.id
    }    

    return resp