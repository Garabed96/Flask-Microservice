from flask import Flask, Blueprint
from flask_cors import CORS
from project.models import db
import os
from dotenv import load_dotenv

load_dotenv('.env')  # take environment variables from .env.
def create_app(test_config=None):
    # Create the Flask app
    app = Flask(__name__)

    # Configure the app
    # config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    register_blueprints(app)
    ##Connect to Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

def register_blueprints(app):
    from project.users import users_blueprint
    app.register_blueprint(users_blueprint)