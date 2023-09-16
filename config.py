import os
from dotenv import load_dotenv

load_dotenv('.env')  # take environment variables from .env.

# Determine the folder of the top-level directory of this project

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DEVELOPMENT_DATABASE_URI")


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    # If were in production mode, replace the DEVELOPMENT_DATABASE_URI with the PRODUCTION_DATABASE_URI
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DEPLOYMENT_DATABASE_URI')
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


class ProductionConfig(Config):
    FLASK_ENV = 'production'



class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TESTING_DATABASE_URI")
    WTF_CSRF_ENABLED = False
