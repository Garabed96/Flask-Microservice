from project import create_app

# Call the create_app() function to start the Flask app
# used for the development server config
app = create_app()
app.run(debug=True, host='0.0.0.0', port=8000)