import json
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    passkey = os.getenv('PASSKEY')
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


class MpesaAccessToken:
    token_response = requests.get(
        Credentials.api_url, 
        auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret)
    )
    try:
        access_token = json.loads(token_response.text)
        validated_token = access_token['access_token']
    except (json.JSONDecodeError, KeyError):
        validated_token = None  # If there's an issue parsing the response or missing 'access_token'


class MpesaPassword:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = "174379"
    passkey = Credentials.passkey

    encode_str = (shortcode or '') + (passkey or '') + (timestamp or '')
    encoded = base64.b64encode(encode_str.encode('utf-8'))
    decoded_password = encoded.decode('utf-8')
