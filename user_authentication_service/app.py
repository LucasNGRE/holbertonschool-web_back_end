#!/usr/bin/env python3
"""App module
"""
from flask import Flask, jsonify, request
from auth import Auth
import bcrypt
from user import User
from db import DB


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue"}), 200


AUTH = Auth()


@app.route('/users', methods=['POST'])
def register_user():
    """Register a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
