import os
import secrets
from datetime import timedelta

class Config:
    # Basic Flask config
    DEBUG = os.getenv("FLASK_ENV") == "development"
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_urlsafe(32))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=8)
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False 