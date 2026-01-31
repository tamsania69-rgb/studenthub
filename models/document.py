class document:
    def __init__(self, id, course_id, title, doc_type, content=None):
        self.id = id
        self.course_id = course_id                      # cle étrangère vers le cours associé au document
        self.title = title
        self.doc_type = doc_type
        self.content = content

    def __str__(self):
        return f"Document(id={self.id}, title='{self.title}', course_id={self.course_id}, doc_type='{self.doc_type}')"