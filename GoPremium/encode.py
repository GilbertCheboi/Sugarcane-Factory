import base64
from django.conf import settings
from . import keys
def generate_password(date):
    data_to_encode = keys.LIPA_NA_MPESA_PASSKEY + keys.BUSINESS_SHORTCODE + date

    encoded_string = base64.b64encode(data_to_encode.encode())

    decode_password = encoded_string.decode("utf-8")

    return decode_password  