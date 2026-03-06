from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int


class StudentManager:
    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, name: str, age: int) -> None:
        self.students.append(Student(name=name, age=age))

    def list_students(self) -> list[Student]:
        return self.students

    def find_student(self, name: str) -> Student | None:
        for student in self.students:
            if student.name == name:
                return student
        return None
