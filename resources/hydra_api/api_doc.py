import crud
import ctx
import templates
import json
from . import hydra

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


class APIDocumentation(crud.CRUD):
    data = {}
    location = "/api/vocab"

    def getAll(self):
        content = templates.render({
                "base_url": ctx.base_url
            },"doc.json")
        api = json.loads(content)
        api["supportedClass"] += [obj.toJSON() for obj in hydra.get_classes()]


        for classObj in hydra.get_entrypoint_classes():
            for apiClass in api["supportedClass"]:
                if apiClass["@id"] == "vocab:EntryPoint":
                    apiClass["supportedProperty"].append(classObj.getEntryPointDoc())
                    break

        api = json.loads(json.dumps(api, default=dumper, indent=2))
        return ctx.success(api, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: APIDocumentation())