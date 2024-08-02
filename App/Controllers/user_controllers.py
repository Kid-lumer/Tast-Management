from flask import Flask, jsonify, session, request, redirect, url_for, flash, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from ..Models.user import User
from flask_bcrypt import Bcrypt


def signup():
    data = request.get_json()
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists
    if username in User:
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the password before storing it
    hashed_password = Bcrypt.generate_password_hash(password).decode('utf-8')
    
    # Create a new user
    new_user = {'name': name, 'password': hashed_password}
    
    # Assign a user ID (You might need to handle this with a database)
    user_id = len(User) + 1
    User[username] = {'user_id': user_id, 'name': name, 'password': hashed_password}

    return jsonify({'message': 'User registered successfully'}), 201