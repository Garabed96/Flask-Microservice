"""
The Users Blueprint handles the CRUD of Users for the users of this application.
"""
from flask import Blueprint

users_blueprint = Blueprint('users', __name__, template_folder='templates')

from project.users import routes