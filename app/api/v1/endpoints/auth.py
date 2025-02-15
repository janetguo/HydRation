from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User, db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
        
    user = User.query.filter_by(email=username).first()
    
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token, token_type="bearer")
    
    return jsonify({"error": "Invalid credentials"}), 401 