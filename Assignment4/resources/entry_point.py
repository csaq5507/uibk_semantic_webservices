import crud

class EntryPoint(crud.CRUD):
    data = {}
    location = "/api"
    raw_data = True
    
    def __init__(self):
        pass
    
crud.register(lambda: EntryPoint())