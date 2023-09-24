import os
import pytest

from project import create_app
from project.models import User

# Testing blog example from:
# https://testdriven.io/blog/flask-pytest/#why-write-tests

# -------------------
# Fixtures
# -------------------

@pytest.fixture(scope='module')
def new_user():
    user = User(email='testuser@gmail.com',
                name='doom',
                password='password',
                weight_value=190,
                weight_unit='lb',
                height_value=185,
                height_unit='cm',
                membership_status='basic'
                )
    return user

@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to create the Flask app
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask app configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!
