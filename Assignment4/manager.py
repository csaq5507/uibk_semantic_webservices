
import db
import ctx

registered_resources = {}

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



    