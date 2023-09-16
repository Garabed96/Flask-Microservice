from project import create_app

def test_home_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Set the Testing configuration prior to create the Flask app
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Welcome to the home page!' in response.data
        assert b'Need an account?' in response.data
        assert b'Already have an account?' in response.data

    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the home page!' in response.data