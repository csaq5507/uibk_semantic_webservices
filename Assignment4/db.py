import uuid
import ctx

def requires(json, properties):
    for (i, name) in enumerate(properties):
        if name not in json:
            return (False, "Missing property {}".format(name), i + 1)
    return (True, "")

def next_id():
    return str(str(uuid.uuid4())[:8])

class Database:
    def __init__(self):
        self.data = {}

    def getAll(self, crud):
        if crud.location not in self.data:
           self.data[crud.location] = {}

        if crud.raw_data:
            return ctx.success(self.data[crud.location], 200)

        items = []
        for key in self.data[crud.location].keys():
            entry = crud.create_entry(self.data[crud.location][key], key)
            items.append(entry)

        return ctx.success(items, 200)

    def get(self, crud):
        if crud.location not in self.data:
           self.data[crud.location] = {}

        if crud.id not in self.data[crud.location]:
            return ctx.error("Entry not found", 1, 404)

        return ctx.success(self.data[crud.location][crud.id], 200)

    def add(self, crud):
        if crud.location not in self.data:
            self.data[crud.location] = {}

        if crud.id in self.data[crud.location]:
            return ctx.error("Entry already exists", 1, 400)

        self.data[crud.location][crud.id] = crud.data

        return ctx.success(crud.dump(), 201)

    def update(self, crud):
        if crud.location not in self.data:
            self.data[crud.location] = {}

        if crud.id not in self.data[crud.location]:
            return ctx.error("Entry not found", 1, 404)

        current_data = self.data[crud.location][crud.id]
        for key in crud.data:
            if key not in current_data:
                return ctx.error("Bad field {}".format(key), 1, 400)
            current_data[key] = crud.data[key]

        self.data[crud.location][crud.id] = current_data
        
        crud.data = current_data
        return ctx.success(crud.dump(), 200)
        
    def delete(self, crud):
        if crud.location not in self.data:
            self.data[crud.location] = {}

        if crud.id not in self.data[crud.location]:
            return ctx.error("Entry not found", 1, 404)

        del self.data[crud.location][crud.id]

        return ctx.success()








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