import json
import ctx
from flask import request
from .supportedClass import HydraClass

VOCAB_URL = "{}/api/vocab".format(ctx.base_url)
LINK_HEADER = { 
    "link": '<{}>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"'.format(VOCAB_URL)
}

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.data

registered_resources = {}
registered_classes = {}
registered_entry_point_classes = {}


def onContext():
    global registered_classes

    method = str(request.method).lower()
    rule = str(request.url_rule)
    ctxName = rule.replace("/api/contexts/", "").replace(".jsonld", "")

    classes = [obj for obj in registered_classes.values() if obj.contextName == ctxName]
    
    if len(classes) == 0:
        return ctx.error("unknown resource", 1, 404)
    
    obj = classes[0]
    context_json = {
        "@context": obj.apiContext
    }

    context_json["@context"]["hydra"] = "http://www.w3.org/ns/hydra/core#"
    context_json["@context"]["vocab"] = VOCAB_URL + "#"

    return ctx.success(context_json, 200, headers = LINK_HEADER)


def onOperation(id = None):
    global registered_resources
    method = str(request.method).lower()
    rule = str(request.url_rule)

    if rule not in registered_resources:
        return ctx.error("unknown resource", 1, 404)
    
    obj = registered_resources[rule] 
    foundOperations = [operation for operation in obj.getOperations() if operation.getMethod().lower() == method]    

    if len(foundOperations) == 0:
        return ctx.error("Method not allowed", 1, 405)

    for op in obj.getOperations():
        print(obj.resource_name, op.getMethod())

    if len(foundOperations) != 1:
        return ctx.error("Mutiple operations found", 1, 500)

    opObj = foundOperations[0]
    op = foundOperations[0].operation
    if method == "get" and id:
        return op(id, opObj)
    if method == "get":
        return op(opObj)
    if method == "option":
        return op(opObj)
    elif method == "post":
        return op(request.get_json(), opObj)
    elif method == "put" and id:
        return op(request.get_json(), id, opObj)
    elif method == "delete" and id:
        return op(id, opObj)

def register_class(obj: HydraClass):
    global registered_resources
    global registered_classes

    name = obj.resource_name
    id = obj.get_id()
    if id in registered_classes:
        return 
    registered_classes[id] = obj
        
    urls = [
        name,
        name + "/",
    ]

    view_func = onOperation
    view_func.methods = ['GET', 'POST', 'PUT', 'DELETE']

    for operation in obj.getOperations():
        for url in urls:
            ctx.app.add_url_rule(url, name, view_func)
        
    if obj.contextName:
        ctx_url = "/api/contexts/{}.jsonld".format(obj.contextName)
        print("registered Context at:", ctx_url)
        ctx.app.add_url_rule(ctx_url, ctx_url, onContext)

    for url in urls:
        registered_resources[url] = obj

def get_classes():
    global registered_classes
    return registered_classes.values()


def add_to_entrypoint(classObj: HydraClass):
    global registered_entry_point_classes
    registered_entry_point_classes[classObj.get_id()] = classObj
    pass

    
def get_entrypoint_classes():
    global registered_entry_point_classes
    return registered_entry_point_classes.values()