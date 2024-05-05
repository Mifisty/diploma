import os
import requests
from dotenv import load_dotenv

load_dotenv()
login_api = os.getenv('API_LOGIN')
pass_api = os.getenv('API_PASS')
api_url = os.getenv('API_URL')
headers = {"authorization": "Basic a2F6YW5leHByZXNzLWN1c3RvbWVyOmN1c3RvbWVyU2VjcmV0S2V5",
           'User-Agent': "PostmanRuntime/7.37.3"
           }
json_data = {
    "grant_type": "password",
    "username": login_api,
    "password": pass_api,
}


def api_token():
    api_request = requests.post(api_url + 'oauth/token/', data=json_data, headers=headers)
    return api_request.json()['access_token']
