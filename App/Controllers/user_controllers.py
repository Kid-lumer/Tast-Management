from flask import Flask, jsonify, session, request, redirect, url_for, flash, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from ..Models.user import User
from flask_bcrypt import Bcrypt


def signup():
    user = {
    "full_name" : request.json.get('full_name'),
    "email" : request.json.get('email'),
    "cell_number" : request.json.get('cell_number'),
    "password" : request.json.get('password')
    }

    # Check if username already exists
    User.create_user(user)
    return jsonify({'message': 'succes'}), 400

def login():
    user_details = {
        "email" : request.json.get('email'),
        "password" : request.json.get('password')
    }    
    User.find_user_by_email
    return jsonify('message': 'login success' )