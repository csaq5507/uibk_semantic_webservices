
import db
import ctx
from flask import request

registered_resources = {}

def run(id=None):
    global registered_resources
    method = str(request.method)
    rule = str(request.url_rule)
    print(rule)
    if rule not in registered_resources:
        return ctx.error("unknown resource", 1, 404)
    
    obj = registered_resources[rule]()
    obj.setup()
    if method == "GET" and id:
        return obj.get(id)
    if method == "GET":
        return obj.getAll()
    if method == "OPTION":
        return obj.option()
    elif method == "POST":
        return obj.post(request.get_json())
    elif method == "PUT":
        return obj.put()
    elif method == "DELETE":
        return obj.delete()

def register_dynamic(creator):
    unified_location = creator().location.rstrip("/")

    view_func = run
    view_func.methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTION']

    ctx.app.add_url_rule(unified_location, unified_location, view_func)
    ctx.app.add_url_rule(unified_location + "/", unified_location, view_func)
    ctx.app.add_url_rule(unified_location + "/<id>", unified_location, view_func)

    registered_resources[unified_location] = creator
    registered_resources[unified_location + "/"] = creator
    registered_resources[unified_location + "/<id>"] = creator

def register(creator):
    global registered_resources

    registered_resources[creator().location] = creator
    
def get_all_resources():
    global registered_resources
    return list(registered_resources.keys())

def invoke(location, method, data = None, id = None):
    global registered_resources

    location = "/" + location

    if location not in registered_resources:
        return ctx.error("unknown resource", 1, 404)

    obj = registered_resources[location]()
    obj.setup()
    if method == "GET" and id:
        return obj.get(id)
    if method == "GET":
        return obj.getAll()
    elif method == "POST":
        return obj.post(data)
    elif method == "PUT":
        return obj.put(data, id)
    elif method == "DELETE":
        return obj.delete(id)



    