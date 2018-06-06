import crud

class Category(crud.CRUD):
    data = {}
    location = "/category"
    
    def __init__(self):
        pass

    def on_create_entry(self):
        return {}
    
crud.register(lambda: Category())