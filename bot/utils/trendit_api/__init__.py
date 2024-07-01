import requests
from json.decoder import JSONDecodeError
from config import Config
from ...utils.helpers import console_log, log_exception

class BackendAPI:
    def __init__(self):
        self.base_url = f"{Config.API_DOMAIN_NAME}/api"
        self.admin_base_url = f"{Config.API_DOMAIN_NAME}/api/admin"
        self.telegram_base_url = f"{Config.API_DOMAIN_NAME}/api/telegram"
        self.token = self.get_jwt_token()
    
    def log_response(self, response):
        try:
            console_log("response", response)
            
            response_data = response.json()
            
            console_log("response_data", response_data)
        except JSONDecodeError as e:
            log_exception("Failed to decode Response", e)
            response = None
            raise e
        

    def get_jwt_token(self):
        login_url = f"{self.base_url}/login"
        
        console_log("login endpoint", login_url)
        console_log("email_username", Config.BOT_APP_USERNAME)
        
        credentials = {
            "email_username": Config.BOT_APP_USERNAME,
            "password": Config.BOT_PASSWORD
        }
        try:
            response = requests.post(login_url, json=credentials)
            console_log("response", response)
            
            response_data = response.json()
            console_log("response_data", response_data)
        except JSONDecodeError as e:
            log_exception("Failed to obtain JWT token", e)
        
        if response.status_code == 200:
            return response_data.get('access_token')
        else:
            raise Exception("Failed to obtain JWT token")

    def fetch_tasks(self):
        url = f"{self.base_url}/tasks"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.get(url, headers=headers)
            
            self.log_response(response)
            
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None

    def approve_task(self, task_id):
        url = f"{self.admin_base_url}/tasks/{task_id}/approve"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.post(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None

    def reject_task(self, task_id):
        url = f"{self.admin_base_url}/tasks/{task_id}/reject"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.post(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None

    def webhook_get_pending_social_profiles(self):
        url = f"{self.telegram_base_url}/pending-socials"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.post(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data
    
    def approve_social_profile(self, profile_id):
        url = f"{self.admin_base_url}/social-profiles/{profile_id}/approve"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.post(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None
    
    def reject_social_profile(self, profile_id):
        url = f"{self.admin_base_url}/social-profiles/{profile_id}/reject"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.post(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None

    def fetch_wallet_balance(self):
        url = f"{self.admin_base_url}/balance"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.get(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None

    def fetch_stats(self):
        url = f"{self.admin_base_url}/stats"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = requests.get(url, headers=headers)
            self.log_response(response)
            response_data = response.json()
        except JSONDecodeError as e:
            console_log("Failed to decode Response", e)
        
        return response_data if response.status_code == 200 else None
    
    