import crud

class Author(crud.CRUD):
    data = {}
    location = "/authors"
    
    def __init__(self):
        pass

    def on_create_entry(self):
        return {
            "name": self.data["name"]
            }
    
crud.register(lambda: Author())