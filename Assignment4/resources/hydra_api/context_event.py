import crud
import ctx
import templates
import json
import hydra

class Context_Event(crud.CRUD):
    data = {}
    location = "/api/contexts/Event.jsonld"

    def getAll(self):
        return ctx.success({
                "@context":{
                    "hydra": "http://www.w3.org/ns/hydra/core#",
                    "vocab": hydra.VOCAB_URL + "#",
                    "Event": "http://schema.org/Event",
                    "name": "http://schema.org/name",
                    "description": "http://schema.org/description",
                    "start_date":{
                        "@id": "http://schema.org/startDate",
                        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    },
                    "end_date":{
                        "@id": "http://schema.org/endDate",
                        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
                    }
                }
            }, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: Context_Event())