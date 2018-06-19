import crud
from field import Field

class Event(crud.CRUD):
    data = {}
    location = "/events"

    def on_create_entry(self):
        return {
            "title": self.data["title"],
            "date": self.data["date"]
            }

crud.register(lambda: Event())