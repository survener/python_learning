class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name: str, age: int):
        self.students.append({"name": name, "age": age})

    def list_students(self):
        return self.students

    def find_student(self, name: str):
        for s in self.students:
            if s["name"] == name:
                return s
        return None