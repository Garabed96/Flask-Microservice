from project import create_app
import os
import json
CREATE_USER = 'http://127.0.0.1:8000/adduser'
from faker import Faker
def test_create_new_user():
    """
      GIVEN a Flask application configured for testing
      WHEN the '/' page is requested (GET)
      THEN check that the response is valid
      """
    # Set the Testing configuration prior to create the Flask app
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Initialize Faker object
    fake = Faker()
    unique_email = fake.email()
    unique_name = fake.name()
    # Creating a dummy payload
    payload = {
        "name": unique_name,
        "email": unique_email,
        "password": "010101010",
        "membership_status": "DOOM",
        "weight_value": "130",
        "weight_unit": "kg",
        "height_value": "184",
        "height_unit": "cm"
    }
    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post(CREATE_USER, json=payload)

        # Check the response status code
        assert response.status_code == 201

        # Check the response JSON or other relevant data
        response_data = json.loads(response.data)
        assert response_data['message'] == "User created successfully"