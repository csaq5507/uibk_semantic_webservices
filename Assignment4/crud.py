
import db
import manager
import ctx

myDB = db.db

class CRUD:
    id = db.next_id()
    data = {}
    raw_data = False
    
    def __init__(self):
        pass
        
    def setup(self):
        pass

    def on_create_entry(self):
        return {}
        
    def create_entry(self, data, id):
        self.data = data
        self.id = id
        base_entry = { 
            "id": id,
            "self": "{}{}/{}".format(ctx.base_url, self.location, id)
         }

        custom_entry = self.on_create_entry()
        combined = dict(base_entry)
        combined.update(custom_entry)
        return  combined



    def dump(self):
        data = self.data
        data["id"] = self.id
        return data

    def getAll(self):
        return myDB.getAll(self)

    def get(self, id):
        self.id = id
        return myDB.get(self)

    def post(self, data):
        self.data = data
        return myDB.add(self)

    def put(self, data, id):
        self.id = id
        self.data = data
        return myDB.update(self)
        
    def delete(self, id):
        self.id = id
        return myDB.delete(self)

    
def register(creation_func):
    manager.register(creation_func)

def register_dynamic(creation_func):
    manager.register_dynamic(creation_func)
