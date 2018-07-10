import crud
import ctx
import templates
import json
from . import hydra

class EntryPoint(crud.CRUD):
    data = {}
    location = "/api"

    def getAll(self):
        payload = {
                "@context": "/api/contexts/EntryPoint.jsonld",
                "@id": "/api/",
                "@type": "EntryPoint"
            }

        for classObj in hydra.get_entrypoint_classes():
            name = classObj.getEntryPointName()
            payload[name] = classObj.resource_name + "/"

        return ctx.success(payload, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: EntryPoint())