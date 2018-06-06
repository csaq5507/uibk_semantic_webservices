

class Field:
    def __init__(self, name, value, required=False):
        self.name = name
        self.value = value
        self.required = required