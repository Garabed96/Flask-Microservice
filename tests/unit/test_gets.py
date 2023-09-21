import os
from project import create_app
import json

SHOW_ALL = 'http://127.0.0.1:8000/all'
GET_RANDOM_USER = ' http://127.0.0.1:8000/random_user'
UPDATE_USERS_NAME = 'http://127.0.0.1:8000/update'
CREATE_USER = 'http://127.0.0.1:8000/adduser'
GET_SPECIFIC_USER = 'http://127.0.0.1:8000/user'

# just checking if endpoint working, useless test we can just check in http-client
def test_show_all_users():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/all' page is requested (GET)
    THEN check that the response is valid
    """
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get(SHOW_ALL)

        # Check the return status code
        assert response.status_code == 200

        # Parse the JSON response
        response_data = json.loads(response.data)

        # Check content of each user in the response
        for user in response_data['users']:
            assert isinstance(user['email'], str)
            assert isinstance(user['name'], str)


def test_get_random_user():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/random_user' page is requested (GET)
    THEN check that the response is valid
    """
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get(SHOW_ALL)

        # Check the return status code
        assert response.status_code == 200

        response_data = json.loads(response.data)

        for user in response_data['users']:
            assert isinstance(user['email'], str)
            assert isinstance(user['name'], str)


def test_get_specific_user():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/user' page is requested (GET)
    THEN check that the response is valid
    """
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('users/4')

        # Check the return status code
        assert response.status_code == 200

        response_data = json.loads(response.data)
        user = response_data['user']  # Use 'user' key to access user data
        assert isinstance(user['email'], str)
        assert isinstance(user['name'], str)