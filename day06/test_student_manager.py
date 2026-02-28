from student_manager import StudentManager


def test_add_and_find_student():
    sm = StudentManager()
    sm.add_student("Alice", 20)
    assert sm.find_student("Alice") == {"name": "Alice", "age": 20}


def test_find_missing_student():
    sm = StudentManager()
    assert sm.find_student("Bob") is None


def test_list_students_count():
    sm = StudentManager()
    sm.add_student("A", 18)
    sm.add_student("B", 19)
    assert len(sm.list_students()) == 2