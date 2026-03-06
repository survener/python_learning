import pytest
from todo_store import (
    load_tasks,
    save_tasks,
    add_task,
    finish_task,
    InvalidTodoDataError,
)


def test_load_missing_file(tmp_path):
    p = tmp_path / "todo.json"
    assert load_tasks(str(p)) == []


def test_save_and_load(tmp_path):
    p = tmp_path / "todo.json"
    tasks = []
    add_task(tasks, "learn git")
    add_task(tasks, "learn python")
    save_tasks(str(p), tasks)

    loaded = load_tasks(str(p))
    assert len(loaded) == 2
    assert loaded[0]["title"] == "learn git"


def test_finish_task():
    tasks = [{"title": "a", "done": False}]
    ok = finish_task(tasks, 1)
    assert ok is True
    assert tasks[0]["done"] is True


def test_invalid_json_raises_custom_error(tmp_path):
    p = tmp_path / "todo.json"
    p.write_text("{bad json", encoding="utf-8")

    with pytest.raises(InvalidTodoDataError):
        load_tasks(str(p))


def test_non_list_json_raises_custom_error(tmp_path):
    p = tmp_path / "todo.json"
    p.write_text('{"title": "not-a-list"}', encoding="utf-8")

    with pytest.raises(InvalidTodoDataError):
        load_tasks(str(p))


#new addition apart:

def test_load_empty_file(tmp_path):
    p = tmp_path / "todo.json"
    p.write_text("", encoding="utf-8")
    assert load_tasks(str(p)) == []


def test_finish_task_invalid_index():
    tasks = [{"title": "a", "done": False}]
    assert finish_task(tasks, 0) is False
    assert finish_task(tasks, 2) is False
