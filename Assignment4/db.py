import uuid

def requires(json, properties):
    for (i, name) in enumerate(properties):
        if name not in json:
            return (False, "Missing property {}".format(name), i + 1)
    return (True, "")

def next_id():
    return str(uuid.uuid4())[:8]

class Database:
    def __init__(self):
        self.events = {}

    def get_events(self):
        return self.events

    def add_event(self, entry):
        valid = requires(entry, ["name", "date"])
        if not valid[0]:
            return valid

        id = next_id()
        entry["id"] = id
        self.events[id] = entry

        return (True, entry)


db = Database()