import requests
from requests.auth import HTTPBasicAuth
from . import keys

def generate_access_token():
    res = requests.get(keys.ACCESS_TOKEN_URL, auth=HTTPBasicAuth(keys.CONSUMER_KEY, keys.CONSUMER_SECRET))
    json_response = res.json()

    access_token = json_response["access_token"]

    return access_token