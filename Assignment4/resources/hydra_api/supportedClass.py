
import json
from .supportedOperation import HydraOperation
from .supportedProperty import HydraProperty
from . import hydra


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

class HydraClass(object):
    def __init__(self, 
                id = "http://schema.org/Event", 
                title = "Event", 
                desc = None,   
                subClassOf = None,
                label = None,
                resource_name = None,
                context_location = None):
        
        self.data = {
            "@id": "http://schema.org/Event",
            "@type": "hydra:Class",
            "hydra:title": "Event",
            "hydra:description": None,
            "supportedOperation": [],
            "supportedProperty": []
        }

        self.context_location = context_location
        self.data["@id"] = id
        self.data["hydra:title"] = title
        self.data["hydra:description"] = desc
        self.contextName = None

        if subClassOf:
            self.data["subClassOf"] = subClassOf
        
        if label:
            self.data["hydra:label"] = label

        self.resource_name = resource_name
        self.entryPointDoc = None
        self.entryPointName = None

    def setEntryPointName(self, name):
        self.entryPointName = name

    def getEntryPointName(self):
        return self.entryPointName

    def setEntryPointDoc(self, doc):
        self.entryPointDoc = doc

    def getEntryPointDoc(self):
        return self.entryPointDoc

    def get_resource_name(self):
        return self.resource_name

    def get_id(self):
        return self.data["@id"]

    def setContextName(self, name):
        self.contextName = name

    def setContext(self, apiContext):
        self.apiContext = apiContext

    def getOperations(self):
        return self.data["supportedOperation"]

    def addOperation(self, operation: HydraOperation):
        operation.hydraClass = self
        self.data["supportedOperation"].append(operation)

    def addProperty(self, prop: HydraProperty):
        self.data["supportedProperty"].append(prop)

    def toJSON(self):
        return self.data