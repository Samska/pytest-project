import requests
from config import API_BASE_URL

def create_user(user_data):
    user_endpoint = f"{API_BASE_URL}/usuarios"
    response = requests.post(user_endpoint, json=user_data)
    return response

def get_user(user_id):
    user_endpoint = f"{API_BASE_URL}/usuarios/{user_id}"
    response = requests.get(user_endpoint)
    return response

def get_users():
    user_endpoint = f"{API_BASE_URL}/usuarios"
    response = requests.get(user_endpoint)
    return response

def update_user(user_id, updated_user_data):
    user_endpoint = f"{API_BASE_URL}/usuarios/{user_id}"
    response = requests.put(user_endpoint, json=updated_user_data)
    return response

def delete_user(user_id):
    user_endpoint = f"{API_BASE_URL}/usuarios/{user_id}"
    response = requests.delete(user_endpoint)
    return response
