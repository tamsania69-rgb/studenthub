class document:
    def __init__(self, id, title, content=None, course_id=None):
        self.id = id
        self.title = title
        self.content = content
        self.course_id = course_id

    def __str__(self):
        return f"Document(id={self.id}, title='{self.title}', course_id={self.course_id})"