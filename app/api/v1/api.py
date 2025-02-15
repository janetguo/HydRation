from flask import Blueprint
from app.api.v1.endpoints.users import users_bp
from app.api.v1.endpoints.auth import auth_bp

api_bp = Blueprint("api", __name__)

# Register endpoint blueprints
api_bp.register_blueprint(auth_bp)
api_bp.register_blueprint(users_bp, url_prefix="/users") 