# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Ensure you have a config.py with Config class

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints or routes
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
