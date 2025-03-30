import requests, os
from flask import jsonify

URL = os.environ.get('API_URL_USERS')
API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

def headerType():
    return {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

def get_user(username, password):
    headers = headerType()
    apiResponse = requests.get(URL, headers=headers) 

    if apiResponse.status_code != 200:
        return {"error": "Failed to get API data", "status_code": apiResponse.status_code}

    users = apiResponse.json()
    user = None

    for u in users:
        if u['username'] == username and u['password'] == password:
            user = u

    if user:
        print('Found user:', user)
        return user
    else:
        print('No user matches in DB')
        return None

def create_user():
    return