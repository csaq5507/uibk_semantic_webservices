#!flask/bin/python
from flask import Flask, jsonify, request, Response

def success(response = None, status_code = 200, code = 0, plain = True):
    if plain:
        return (jsonify(response), status_code, {'Content-Type': 'application/ld+json'})


    if response != None:
        return (jsonify({"code": code, "response": response}), status_code, {'Content-Type': 'application/ld+json'})
    else:
        return (jsonify({"code": code}), status_code, {'Content-Type': 'application/ld+json'})

def success_created(response = None, status_code = 201, code = 0):
    return success(response, status_code, code)
    
def error(message = "", code = 1, status_code = 400):
    return (jsonify({"code": code, "message": message}), status_code, {'Content-Type': 'application/ld+json'})

app = Flask(__name__)
base_url = "http://localhost:5000"

def run_app():
    app.run(debug=True)
    