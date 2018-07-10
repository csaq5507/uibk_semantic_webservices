import crud
import ctx
import templates
import json
from . import hydra

class Contexts(crud.CRUD):
    data = {}
    location = "/api/contexts/EntryPoint.jsonld"

    def getAll(self):
        payload = {
                "@context":{
                    "hydra": "http://www.w3.org/ns/hydra/core#",
                    "vocab": hydra.VOCAB_URL + "#",
                    "EntryPoint": "vocab:EntryPoint",
                    "events":{
                        "@id": "vocab:EntryPoint/events",
                        "@type": "@id"
                    },
                    "actors":{
                        "@id": "vocab:EntryPoint/actors",
                        "@type": "@id"
                    },
                    "locations":{
                        "@id": "vocab:EntryPoint/locations",
                        "@type": "@id"
                    },
                    "reviews":{
                        "@id": "vocab:EntryPoint/reviews",
                        "@type": "@id"
                    },
                    "ratings":{
                        "@id": "vocab:EntryPoint/ratings",
                        "@type": "@id"
                    },
                    "authors":{
                        "@id": "vocab:EntryPoint/authors",
                        "@type": "@id"
                    }
                }
            }

        for classObj in hydra.get_entrypoint_classes():
            name = classObj.getEntryPointName()
            payload["@context"][name] = {
                "@id": "vocab:EntryPoint/{}".format(name),
                "@type": "@id"
            }

        return ctx.success(payload, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: Contexts())