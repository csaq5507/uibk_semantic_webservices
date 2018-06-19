import crud
import ctx
import templates
import json
import hydra

class Context_EventCollection(crud.CRUD):
    data = {}
    location = "/api/contexts/EventCollection.jsonld"

    def getAll(self):
        return ctx.success({
                "@context":{
                    "hydra": "http://www.w3.org/ns/hydra/core#",
                    "vocab": hydra.VOCAB_URL + "#",
                    "EventCollection": "vocab:EventCollection",
                    "members": "http://www.w3.org/ns/hydra/core#member"
                }
            }, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: Context_EventCollection())