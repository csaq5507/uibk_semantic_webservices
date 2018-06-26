#!flask/bin/python

import ctx
from flask import jsonify, request

from resources import index
from resources import event
from resources import location
from resources import author
from resources.hydra_api import entry_point
from resources.hydra_api import context_entry_point
from resources.hydra_api import api_doc

# from resources.hydra_api.actor import actor
# from resources.hydra_api.actor import actor_collection

# from resources.hydra_api.location import location
# from resources.hydra_api.location import location_collection

# from resources.hydra_api.rating import rating
# from resources.hydra_api.rating import rating_collection

from resources.hydra_api.review import event_collection
from resources.hydra_api.review import actor_collection
from resources.hydra_api.review import author_collection
from resources.hydra_api.review import review_collection
from resources.hydra_api.review import rating_collection
from resources.hydra_api.review import location_collection


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