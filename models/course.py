class course:
    def __init__(self, id, name, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Course(id={self.id}, name='{self.name}', description='{self.description}')"