from flask import Flask, render_template, jsonify, request
import requests
from api_users import get_user

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login_user')
def login_user():
    return

@app.route('/get_user', methods=['POST'])
def fetch_user_data():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"Error": "Username and password required."}), 400

    user = get_user(username, password)

    if not user:
        return jsonify({"Error": "Invalid credentials"}), 401

    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)