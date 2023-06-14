from flask import Flask # flask is library name, Flask is class in flask library

app = Flask(__name__)
# print(__name__)

# remember that @ is decorator
@app.route("/")
def hello_world():
    return "hello world"