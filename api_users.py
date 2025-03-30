import requests, os
from flask import jsonify

URL = os.environ.get('API_URL_USERS')
API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

def headerType(apiAuthType):
    headers = {
        "apikey": apiAuthType,
        "Content-Type": "application/json"
    }
    return headers

def get_user():
    headers = headerType(API_KEY)
    apiResponse = requests.get(URL, headers=headers) 

    if apiResponse.status_code == 200:
        extracted_apiResponse = []

        for row in apiResponse.json():
            extracted_apiResponse.append({
                'id': row.get('id'),
                'username': row.get('username'),
                'password': row.get('password'),
                'email': row.get('email'),
                'first_name': row.get('first_name'),
                'last_name': row.get('last_name'),
                'date_created': row.get('date_created'),
                'last_password_change': row.get('last_password_change'),
                'last_login': row.get('last_login'),
                'is_active': row.get('is_active'),
                'is_locked': row.get('is_locked')
            })
        
        extracted_apiResponse.sort(key=lambda x: x['id'])

        print('API:', extracted_apiResponse)
        return extracted_apiResponse
    else:
        return {
            "Error": "Failed to get API data", "status code": apiResponse.status_code
        }

def create_user():
    return