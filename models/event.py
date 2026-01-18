class event:
    def __init__(self, id, title, event_type, date=None, description=None):
        self.id = id
        self.title = title
        self.event_type = event_type  # type d'événement (ex: cours, examen_partiel, devoir)
        self.date = date  # date en format string 'JJ-MM-AAAA'
        self.description = description

    def __str__(self):
        return f"Event(id={self.id}, title='{self.title}', event_type='{self.event_type}', date='{self.date}')"