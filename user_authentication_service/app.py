#!/usr/bin/env python3
"""App module
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'])
def login():
    """Logs user in by verifying credentials and creating session."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Logout route. Destroys a session if valid, else 403."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/", 302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
