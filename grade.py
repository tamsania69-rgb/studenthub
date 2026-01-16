class grade:
    def __init__(self, id, student_id, course_id, score):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.score = score

    def __str__(self):
        return f"Grade(id={self.id}, student_id={self.student_id}, course_id={self.course_id}, score={self.score})"