class event:
    def __init__(self, id, title, date=None, description=None):
        self.id = id
        self.title = title
        self.date = date  # date en format string 'YYYY-MM-DD'
        self.description = description

    def __str__(self):
        return f"Event(id={self.id}, title='{self.title}', date='{self.date}')"