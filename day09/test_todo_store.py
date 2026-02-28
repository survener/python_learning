from todo_store import load_tasks, save_tasks, add_task, finish_task


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


def test_finish_task(tmp_path):
    tasks = [{"title": "a", "done": False}]
    ok = finish_task(tasks, 1)
    assert ok is True
    assert tasks[0]["done"] is True