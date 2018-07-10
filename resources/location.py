import crud

class Location(crud.CRUD):
    data = {}
    location = "/locations"
    
    def __init__(self):
        pass

    def on_create_entry(self):
        return {
            "name":    self.data["name"],
            "country": self.data["country"]
            }

    
crud.register(lambda: Location())