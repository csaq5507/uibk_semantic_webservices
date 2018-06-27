import crud
import ctx
import templates
import json
import hydra
import db
from flask import Response

myDB = db.db

class Events(crud.CRUD):
    data = {}
    location = "/api/events"

    def getAll(self):
        events = myDB.getAll_("Event")
        events_ld = json.loads(templates.render({}, "events.json"))
        events_ld["members"] = events
        return ctx.success(events_ld, 200, headers = hydra.LINK_HEADER)

    def get(self, id):
        event = myDB.get_("Event", id)
        if type(event) is Response:
            return event
        return ctx.success(event, 200, headers = hydra.LINK_HEADER)

    def delete(self, id):
        event = myDB.delete_("Event", id)
        if type(event) is Response:
            return event
        return ctx.success({}, 200, headers = hydra.LINK_HEADER)

    def post(self, data):
            
        id = db.next_id()    
        data["@context"] =  "/api/contexts/Event.jsonld"
        data["@id"] =  "/api/events/{}".format(id)
        data["@type"] =  "http://schema.org/Event"

        result = myDB.add_(id, "Event", data)
        if isinstance(result, Response):
            return result

        event_url = "{}/api/events/{}".format(ctx.base_url, id)
        headers = hydra.LINK_HEADER
        headers["location"] = event_url
        headers["content-location"] = event_url
        return ctx.success(data, 201, headers=headers)

    def put(self, data, id):
        event = myDB.replace_("Event", id, data)
        if type(event) is Response:
            return event
        return ctx.success(event, 200, headers = hydra.LINK_HEADER)

    def patch(self, data, id):
        event = myDB.update_("Event", id, data)
        if type(event) is Response:
            return event
        return ctx.success(event, 200, headers = hydra.LINK_HEADER)

crud.register_dynamic(lambda: Events())