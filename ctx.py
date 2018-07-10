#!flask/bin/python
import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

default_content_type = "application/ld+json"

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.data

def success(response = None, status_code = 200, code = 0, plain = True, headers = {}):
    
    if plain:
        r = Response(response=json.dumps(response, default=dumper, indent=2), status=status_code, mimetype=default_content_type)
        r.headers["Content-Type"] = default_content_type
        for header_name in headers:
            r.headers[header_name] = headers[header_name]
        return r

    if response != None:
        return (jsonify({"code": code, "response": response}), status_code, {'Content-Type': default_content_type})
    else:
        return (jsonify({"code": code}), status_code, {'Content-Type': default_content_type})

def success_created(response = None, status_code = 201, code = 0):
    return success(response, status_code, code)
    
def error(message = "", code = 1, status_code = 400, headers=[]):
    response = {"code": code, "message": message}
    r = Response(response=json.dumps(response), status=status_code, mimetype=default_content_type)
    r.headers["Content-Type"] = default_content_type
    for header_name in headers:
        r.headers[header_name] = headers[header_name]
    return r

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

base_url = "http://localhost:5000"

def run_app():
    app.run(debug=True)
    