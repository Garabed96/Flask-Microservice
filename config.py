import os
from dotenv import load_dotenv

load_dotenv('.env')  # take environment variables from .env.

# Determine the folder of the top-level directory of this project

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URI")


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    print("RUNNING DEVELOPMENT CONFIG")
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URI")



class TestingConfig(Config):
    print("TESTING CONFIG RUNNING")
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TESTING_DATABASE_URI")
    WTF_CSRF_ENABLED = False

# Set the default configuration
default_config = DevelopmentConfig