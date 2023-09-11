from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route that responds with "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app if this script is the main program
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
