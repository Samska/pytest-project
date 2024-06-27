import requests
from config import API_BASE_URL

def login(email, password):
    login_endpoint = f"{API_BASE_URL}/login"
    login_data = {
        "email": email,
        "password": password
    }
    response = requests.post(login_endpoint, json=login_data)
    response_json = response.json()
    authorization_token = response_json.get('authorization')
    return response, authorization_token