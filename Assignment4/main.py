#!flask/bin/python

import ctx
from flask import jsonify, request

from resources import index
from resources import event
from resources import location
from resources import author
from resources import entry_point

from resources import mock

import manager

app = ctx.app

@ctx.app.route("/", methods=['GET'])
def index():
    return manager.invoke("", "GET")

@ctx.app.route("/<resource>", methods=['GET'])
def getAll(resource):
    return manager.invoke(resource, "GET")

@ctx.app.route("/<resource>", methods=['POST'])
def post(resource):
    return manager.invoke(resource, "POST", request.json)

@ctx.app.route("/<resource>/<id>", methods=['GET'])
def get(resource, id):
    return manager.invoke(resource, "GET", None, id)

@ctx.app.route("/<resource>/<id>", methods=['PUT'])
def put(resource, id):
    return manager.invoke(resource, "PUT", request.json, id)

@ctx.app.route("/<resource>/<id>", methods=['DELETE'])
def delete(resource, id):
    return manager.invoke(resource, "DELETE", None, id)

if __name__ == "__main__":
    ctx.run_app()