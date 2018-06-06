import crud

class Index(crud.CRUD):
    data = {}
    location = "/"
    raw_data = True
    
    def __init__(self):
        pass

crud.register(lambda: Index())