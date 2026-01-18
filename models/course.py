class course:
    def __init__(self, id, name, semester, year, description=None):
        self.id = id
        self.name = name
        self.semester = semester
        self.year = year
        self.description = description

    def __str__(self):
        return f"Course(id={self.id}, name='{self.name}', semester='{self.semester}', year={self.year}, description='{self.description}')"