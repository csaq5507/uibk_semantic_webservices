import json
from . import supportedOperation
from . import supportedProperty


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


class HydraPropertyInfo:
    def __init__(self,
        id = "vocab:Issue/description", 
        label = "description", 
        desc = "Descripe the property", 
        domain = "vocab:Issue", 
        range = "http://www.w3.org/2001/XMLSchema#string",
        supportedOperations = []):    
        self.data = {
                "@id": id,
                "@type": "rdf:Property",
                "label": label,
                "description": desc,
                "domain": domain,
                "range": range,
                "supportedOperation": supportedOperations
            }
        pass

    def toJSON(self):
        return self.data


class HydraProperty:
    def __init__(self, property: HydraPropertyInfo, title, desc = None, required = True, readonly = False, writeonly = False):    
        self.data = { 
            "property": property,
            "hydra:title": title,
            "hydra:description": desc,
            "required": required,
            "readonly": readonly,
            "writeonly": writeonly
        }
        pass

    def toJSON(self):
        return self.data