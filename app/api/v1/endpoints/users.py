from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.user import User, db

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active
    } for user in users])

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    
    if User.query.filter_by(email=data.get("email")).first():
        return jsonify({"error": "User with this email already exists"}), 400
    
    user = User(
        email=data.get("email"),
        full_name=data.get("full_name")
    )
    user.set_password(data.get("password"))
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "is_active": user.is_active
    }), 201 