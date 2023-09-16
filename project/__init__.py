import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
import os
import sqlalchemy as sa
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv('.env')  # take environment variables from .env.

# -------------------
# Configuration
# -------------------

# Create instance of Flask (Flask-sqlalchemy) in global scope
db = SQLAlchemy()



def create_app():
    # Create the Flask app
    app = Flask(__name__)
    print(os.getenv('CONFIG_TYPE'))
    # Configure the app
    # config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    engine = sa

    register_blueprints(app)
    ##Connect to Database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    inspector = sa.inspect(engine)
    if not inspector.has_table("users"):
        print("CREATING TABLES")
        with app.app_context():
            # db.drop_all()
            db.create_all()
        app.logger.info("CREATING DB TABLES")
    else:
        app.logger.info("TABLES ALREADY CONTAINS USERS TABLE")


    return app


def initialize_extensions(app):
    # since application instance created, pass it to each Flask extension instance to bind it to
    #  the Flask application instance (app)
    db.init_app(app)


def configure_logging(app):
    # Logging Configuration
    if app.config['LOG_WITH_GUNICORN']:
        # Log to stdout
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    else:
        file_handler = RotatingFileHandler('instance/flask-logs.log', maxBytes=10240, backupCount=10)
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask app')


def register_blueprints(app):
    from project.users import users_blueprint
    app.register_blueprint(users_blueprint)