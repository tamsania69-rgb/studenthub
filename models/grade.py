class grade:
    def __init__(self, id, course_id, value, max_value):
        self.id = id
        self.course_id = course_id
        self.value = value
        self.max_value = max_value

    def __str__(self):
        return f"Grade(id={self.id}, course_id={self.course_id}, value={self.value}, max_value={self.max_value})"