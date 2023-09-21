from project import create_app
import os
from dotenv import load_dotenv
load_dotenv('.env')  # take environment variables from .env.
import json
SHOW_ALL = 'http://127.0.0.1:8000/all'

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Set the Testing configuration prior to create the Flask app
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    print(os.environ['CONFIG_TYPE'])
    flask_app = create_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Welcome to the SumPlus App Dashboard' in response.data
        # assert b'Need an account?' in response.data
        # assert b'Already have an account?' in response.data

    # response = test_client.get('/')
    # assert response.status_code == 200
    # assert b'Welcome to the home page!' in response.data


def test_home_page_all():
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

