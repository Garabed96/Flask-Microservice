import logging
from logging.handlers import RotatingFileHandler
from click import echo
from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
import os
import sqlalchemy
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # take environment variables from .env.
BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# -------------------
# Configuration
# -------------------

# Create instance of Flask (Flask-sqlalchemy) in global scope
db = SQLAlchemy()



def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Configure the app
    config_type = os.getenv('CONFIG_TYPE')
    app.config.from_object(config_type)
    print(config_type, "config_type")
    print(f'{app.config["SQLALCHEMY_DATABASE_URI"]}, "SQLALCHEMY_DATABASE_URI"')
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    CORS(app)

    register_blueprints(app)
    initialize_extensions(app)
    configure_logging(app)


    ## Check if dB needs to be initialized
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    if not sqlalchemy.inspect(engine).has_table("USER"):
        print("CREATING TABLES")
        with app.app_context():
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
        file_handler = RotatingFileHandler(f'{BASEDIR}/instance/flask-logs.log', maxBytes=10240, backupCount=10)
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

def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the database."""
        # db.drop_all()
        db.create_all()
        echo('Initialized the database!')