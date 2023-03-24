import requests, json
from . import keys
from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth
from .models import STKPushResponse

unformated_timestamp = datetime.now() 
formated_timestamp = unformated_timestamp.strftime("%Y%m%d%H%M%S") 

data_to_encode = keys.BUSINESS_SHORTCODE + keys.LIPA_NA_MPESA_PASSKEY + formated_timestamp
encoded_data = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_data.decode()

consumer_key = keys.CONSUMER_KEY
consumer_secret = keys.CONSUMER_SECRET

def lipa_na_mpesa():
    # access_token = my_access_token

    # api_url =  "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    # headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.BUSINESS_SHORTCODE,
        "Password": decoded_password,
        "Timestamp": formated_timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.PHONE_NUMBER,
        "PartyB": keys.BUSINESS_SHORTCODE,
        "PhoneNumber": keys.PHONE_NUMBER,
        "CallBackURL": "https://bongasport.com/lipanampesa",
        "AccountReference": "123456",
        "TransactionDesc": "Join premium",
    }

    # res = requests.post(api_url, json=request, headers=headers)
    # mystr = res.text
    # objstr = json.loads(mystr)

    # print(objstr)

    # MerchantRequestID = objstr['MerchantRequestID']
    # CheckoutRequestID = objstr['CheckoutRequestID']
    # ResponseCode = objstr['ResponseCode']
    # ResponseDescription = objstr['ResponseDescription']

    # data= {
    #     "requestId": MerchantRequestID,
    #     "checkoutRequestId": CheckoutRequestID,
    #     "responseCode": ResponseCode,
    #     "responseDescription": ResponseDescription,
    #     }
    
    # stkpush_response = STKPushResponse.objects.create(
    #     merchant_request_id=data['requestId'],
    #     checkout_request_id=data['checkoutRequestId'],
    #     response_code=data['responseCode'],
    #     response_description=data['responseDescription'],
    #     # customer_message=data['CustomerMessage'],
    #     )

    # stkpush_response.save()

    # return data

lipa_na_mpesa()