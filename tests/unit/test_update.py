import os
import json
from project import create_app
from faker import Faker

UPDATE_SPECIFIC_USER = 'http://127.0.0.1:8000/update'

def test_update_user():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/update/{id}' page is requested (PATCH)
    THEN check that the response is valid
    """
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Initialize Faker object
    fake = Faker()
    unique_user = fake.name()
    payload = {"name": unique_user}

    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        # Assuming the user with ID 6 exists in your test database
        response = test_client.patch(UPDATE_SPECIFIC_USER + '/6', json=payload)

        # Check the response status code
        assert response.status_code == 200

        # Check the response JSON
        response_data = response.get_json()
        assert "response" in response_data
        assert response_data["response"]["success"] == "Successfully updated the name."
