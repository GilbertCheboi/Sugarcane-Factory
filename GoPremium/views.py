from .access_token import generate_access_token
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import convert_timestamp
# formated_timestamp = convert_timestamp()
from .encode import generate_password
import requests
from django.conf import settings
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .lipanampesa import lipa_na_mpesa

class Access_token(APIView):
    def get(self, request, format=None):
        access_token = generate_access_token()
        return Response({"access_token": access_token})

class GenereatedPasswordView(APIView):
    def get(self, request, format = None):
        formated_timestamp = convert_timestamp()

        decoded_password = generate_password(formated_timestamp)

        return Response({"password": decoded_password}) 

# Create your views here.
@api_view(['POST'])
def MakePayment(request):
    mpesa_payment = lipa_na_mpesa()
    return Response({"mpesa_payment": mpesa_payment})


# import requests, json
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import PaymentDetailsSerializer
# from . import keys
# from datetime import datetime
# import base64

# from requests.auth import HTTPBasicAuth

# unformated_timestamp = datetime.now() 
# formated_timestamp = unformated_timestamp.strftime("%Y%m%d%H%M%S") 

# data_to_encode = keys.BUSINESS_SHORTCODE + keys.LIPA_NA_MPESA_PASSKEY + formated_timestamp
# encoded_data = base64.b64encode(data_to_encode.encode())
# decoded_password = encoded_data.decode()

# consumer_key = keys.CONSUMER_KEY
# consumer_secret = keys.CONSUMER_SECRET

# api_URL = (
#     "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
# )

# r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
# print(r.text)

# json_response = r.json()

# my_access_token = json_response['access_token']


# @api_view(['POST'])
# def mpesa_stk(request):
#     serializer = PaymentDetailsSerializer(data=request.data)
#     if serializer.is_valid():
#         phone_number = serializer.validated_data['phone_number']
#         # Construct payload for STK push request
#         payload = {
#         "BusinessShortCode": keys.BUSINESS_SHORTCODE,
#         "Password": decoded_password,
#         "Timestamp": formated_timestamp,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": "1",
#         "PartyA": phone_number,
#         "PartyB": keys.BUSINESS_SHORTCODE,
#         "PhoneNumber": phone_number,
#         "CallBackURL": "https://bongasport.com/lipanampesa",
#         "AccountReference": "123456",
#         "TransactionDesc": "Join premium",
#         }
#         # Set headers for STK push request
        
#         access_token = my_access_token

#         api_url =  "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#         headers = {"Authorization": "Bearer %s" % access_token}
#         # Send STK push request
#         response = requests.post(api_url,
#                                  json=payload, headers=headers
#                                  )
#         if response.status_code == status.HTTP_200_OK:
#             # STK push request successful
#             return Response({'message': 'STK push successful'})
#         else:
#             # STK push request failed
#             return Response({'message': 'STK push failed'})
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
