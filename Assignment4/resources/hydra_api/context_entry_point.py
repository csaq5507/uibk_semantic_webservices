import crud
import ctx
import templates
import json
import hydra

class Contexts(crud.CRUD):
    data = {}
    location = "/api/contexts/EntryPoint.jsonld"

    def getAll(self):
        return ctx.success({
                "@context":{
                    "hydra": "http://www.w3.org/ns/hydra/core#",
                    "vocab": hydra.VOCAB_URL + "#",
                    "EntryPoint": "vocab:EntryPoint",
                    "events":{
                        "@id": "vocab:EntryPoint/events",
                        "@type": "@id"
                    }
                }
            }, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: Contexts())