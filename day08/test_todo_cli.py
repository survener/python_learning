from todo_cli import add_task, list_tasks, finish_task


def test_add_and_list():
    tasks = []
    add_task(tasks, "learn python")
    rows = list_tasks(tasks)
    assert rows == ["1. [ ] learn python"]


def test_finish_task_ok():
    tasks = []
    add_task(tasks, "task1")
    assert finish_task(tasks, 1) is True
    assert list_tasks(tasks) == ["1. [x] task1"]


def test_finish_task_invalid():
    tasks = []
    add_task(tasks, "task1")
    assert finish_task(tasks, 2) is False