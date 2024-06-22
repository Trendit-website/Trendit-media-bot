import requests

from config import Config
from ..utils.helpers import log_error

headers ={
    "Authorization": "Bearer {}".format(Config.TELEGRAM_BOT_TOKEN ),
    "Content-Type": "application/json"
}

def trendit_login(data):
    url = f"{Config.API_DOMAIN_NAME}/api/login"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "email_username": data.get("username"),
        "password": data.get("pwd")
    }
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    
    if not response_data:
        log_error("response", response)
        raise Exception("Failed to Login")
    
    return response_data
    