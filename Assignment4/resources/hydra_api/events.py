import crud
import ctx
import templates
import json
import hydra
import db

myDB = db.db

class Events(crud.CRUD):
    data = {}
    location = "/api/events"

    def getAll(self):
        content = templates.render({}, "events.json")
        return ctx.success(json.loads(content), 200, headers = hydra.LINK_HEADER)

    def get(self, id):
        content = templates.render({}, "event.json")
        return ctx.success(json.loads(content), 200, headers = hydra.LINK_HEADER)

    def post(self, data):

        id = myDB.add_event("event", data)
        event_url = "{}/api/events/{}".format(ctx.base_url, id)
        headers = hydra.LINK_HEADER
        headers["location"] = event_url
        headers["content-location"] = event_url

        return ctx.success(data, 201, headers=headers)

crud.register_dynamic(lambda: Events())