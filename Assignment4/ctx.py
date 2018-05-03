#!flask/bin/python
from flask import Flask, jsonify, request

def success(response = None, status_code = 200, code = 0):
    if response:
        return (jsonify({"code": code, "response": response}), status_code)
    else:
        return (jsonify({"code": code}), status_code)

def success_created(response = None, status_code = 201, code = 0):
    return success(response, status_code, code)
    
def error(message = "", code = 1, status_code = 400):
    return (jsonify({"code": code, "message": message}), status_code)

app = Flask(__name__)

def run_app():
    app.run(debug=True)
    