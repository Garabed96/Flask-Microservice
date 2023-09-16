import os

import pytest

from project import create_app, db
from project.models import User


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
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
