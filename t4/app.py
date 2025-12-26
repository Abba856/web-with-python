# install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h2>Welcome to my app</h2>'

# in terminal 
# FLASK_APP=app.py
# FLASK_ENV=development
# flask run