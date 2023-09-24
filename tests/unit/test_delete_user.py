import os
from project import create_app
import json
from unittest.mock import patch
DELETE_SPECIFIC_USER = 'http://127.0.0.1:8000/delete'

def test_delete_user():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/delete/{id}' page is requested (DELETE)
    THEN check that the response is valid
    """
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using Flask app configured for testing
    with flask_app.test_client() as test_client:
        # Mock the dB delete op
        with flask_app.app_context():
            with patch('project.models.User.query.delete') as delete_mock:
                delete_mock.return_value = 1 # simulate that one row was deleted

                response = test_client.delete(DELETE_SPECIFIC_USER + '/4')

                assert response.status_code == 200

                # Check the resp json or other relevant data
                response_data = json.loads(response.data)
                assert response_data['response']['success'] == "Successfully deleted the user."

        # try:
        #     response = test_client.delete(DELETE_SPECIFIC_USER + '/3')
        #
        #
        #     # Check the response status code
        #     assert response.status_code == 200
        #
        #     # Check the response status code
        #
        #     # Check the response JSON or other relevant data
        #     response_data = json.loads(response.data)
        #     assert response_data['response']['success'] == "Successfully deleted the user."
        # except Exception as e:
        #     print(e)
        #     assert False
        #
