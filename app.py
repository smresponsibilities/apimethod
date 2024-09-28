
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 



@app.route('/')
def home():
    return "This is an API method checking API!!"


if __name__ == '__main__':
    app.run(debug=True)