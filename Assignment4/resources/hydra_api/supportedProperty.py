import json
from . import supportedOperation
from . import supportedProperty


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

class HydraProperty:
    def __init__(self, property, title, desc = None, required = True, readonly = False, writeonly = False):    
        self.data = {
            "property": "http://schema.org/name",
            "hydra:title": "name",
            "hydra:description": "The event's name",
            "required": True,
            "readonly": False,
            "writeonly": False
        }
        
        self.data["property"] = property
        self.data["hydra:title"] = title
        self.data["hydra:description"] = desc
        self.data["required"] = True
        self.data["readonly"] = False
        self.data["writeonly"] = False
        pass

    def toJSON(self):
        return self.data