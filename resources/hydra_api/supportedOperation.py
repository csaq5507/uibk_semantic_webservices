import json

class HydraStatusCode:
    def __init__(self, code, desc):
        self.data = {
            "code": 404,
            "description": "If the Event entity wasn't found."
        }
        self.data["code"] = code
        self.data["description"] = desc

    def toJSON(self):
        return self.data

class HydraOperation:

    def __init__(self, 
                id = "_:event_replace", 
                type = "http://schema.org/UpdateAction", 
                method = "GET", 
                label = "Replaces an existing Event entity", 
                expects = "http://schema.org/Event", 
                returns = "http://schema.org/Event",
                operation = None):
        self.data = {
            "@id": "_:event_replace",
            "@type": "http://schema.org/UpdateAction",
            "method": "PUT",
            "label": "Replaces an existing Event entity",
            "description": None,
            "expects": "http://schema.org/Event",
            "returns": "http://schema.org/Event",
            "statusCodes": []
        }

        self.data["@id"] =  id
        self.data["@type"] =  type
        self.data["method"] =  method
        self.data["label"] =  label
        self.data["expects"] =  expects
        self.data["returns"] =  returns
        self.operation = operation

    def getID(self):
        return self.data["@id"]

    def getMethod(self):
        return self.data["method"]

    def getOperations(self):
        return self.operation

    def addStatusCode(self, code: HydraStatusCode):
        self.data["statusCodes"].append(code)

    def toJSON(self):
        return self.data