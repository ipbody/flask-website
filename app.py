from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Main Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'
