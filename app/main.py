from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.core.config import Config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    db.init_app(app)
    jwt.init_app(app)

    # Create database tables
    with app.app_context():
        from app.models.user import User  # Import the model
        db.create_all()

    # Register blueprints
    from app.api.v1.api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    @app.route("/")
    def root():
        return jsonify({"message": "Welcome to FlutterFlow API"})

    @app.route("/health")
    def health_check():
        return jsonify({
            "status": "healthy",
            "version": "1.0.0"
        })

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) 