from project import create_app
import os
# Call the create_app() function to start the Flask app
# used for the development server config
print("RUNNING APP")
print(os.getenv('CONFIG_TYPE'), "CONFIG TYPE")
app = create_app()
# use_reloader = False to prevent the app from restarting after each request, stops from running twice too
# app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'), use_reloader=False)
