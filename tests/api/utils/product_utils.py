import requests
from config import API_BASE_URL

def create_product(product_data, authorization_token):
    product_endpoint = f"{API_BASE_URL}/produtos"
    headers = {
        "Authorization": authorization_token,
        "Content-Type": "application/json"
    }
    response = requests.post(product_endpoint, json=product_data, headers=headers)
    return response

def get_product_by_id(product_id, authorization_token):
    product_endpoint = f"{API_BASE_URL}/produtos/{product_id}"
    headers = {
        "Authorization": authorization_token,
        "Content-Type": "application/json"
    }
    response = requests.get(product_endpoint, headers=headers)
    return response

def update_product(product_id, updated_product_data, authorization_token):
    product_endpoint = f"{API_BASE_URL}/produtos/{product_id}"
    headers = {
        "Authorization": authorization_token,
        "Content-Type": "application/json"
    }

    response = requests.put(product_endpoint, json=updated_product_data, headers=headers)
    return response