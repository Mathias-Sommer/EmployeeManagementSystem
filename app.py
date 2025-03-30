from flask import Flask, render_template, jsonify
from api_users import get_user

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/get_user', methods=['GET'])
def fetch_user_data():
    data = get_user()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)