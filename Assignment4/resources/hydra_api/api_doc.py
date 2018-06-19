import crud
import ctx
import templates
import json
import hydra

class APIDocumentation(crud.CRUD):
    data = {}
    location = "/api/vocab"

    def getAll(self):
        content = templates.render({
                "base_url": ctx.base_url
            },"doc.json")
        return ctx.success(json.loads(content), 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: APIDocumentation())