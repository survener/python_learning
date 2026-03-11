from todo_cli import add_task, list_tasks, finish_task, delete_task, edit_task, search_tasks


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


#new additions apart:

def test_list_tasks_empty():
    tasks = []
    assert list_tasks(tasks) == []


def test_finish_task_zero_index():
    tasks = []
    add_task(tasks, "task1")
    assert finish_task(tasks, 0) is False

def test_delete_task_ok():
    tasks = []
    add_task(tasks, "task1")
    assert delete_task(tasks, 1) is True
    assert list_tasks(tasks) == []


def test_edit_task_ok():
    tasks = []
    add_task(tasks, "old")
    assert edit_task(tasks, 1, "new") is True
    assert list_tasks(tasks) == ["1. [ ] new"]


def test_search_tasks():
    tasks = []
    add_task(tasks, "learn python")
    add_task(tasks, "learn git")
    add_task(tasks, "cook dinner")
    rows = search_tasks(tasks, "learn")
    assert len(rows) == 2


def test_delete_task_invalid_index():
    tasks = []
    add_task(tasks, "task1")
    assert delete_task(tasks, 0) is False
    assert delete_task(tasks, 2) is False


def test_edit_task_invalid_index():
    tasks = []
    add_task(tasks, "task1")
    assert edit_task(tasks, 0, "x") is False
    assert edit_task(tasks, 2, "x") is False


def test_search_tasks_empty_keyword():
    tasks = []
    add_task(tasks, "learn python")
    assert search_tasks(tasks, "") == []
