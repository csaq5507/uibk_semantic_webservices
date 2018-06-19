import crud
import ctx
import templates
import json
import hydra

class EntryPoint(crud.CRUD):
    data = {}
    location = "/api"

    def getAll(self):
        return ctx.success({
                "@context": "/api/contexts/EntryPoint.jsonld",
                "@id": "/api/",
                "@type": "EntryPoint",
                "events": "/api/events/"
            }, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: EntryPoint())