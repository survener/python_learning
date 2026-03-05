import json
from pathlib import Path


Task = dict[str, object]


class TodoStoreError(Exception):
    pass


class InvalidTodoDataError(TodoStoreError):
    pass


def load_tasks(file_path: str) -> list[Task]:
    p = Path(file_path)
    if not p.exists():
        return []

    text = p.read_text(encoding="utf-8").strip()
    if not text:
        return []

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise InvalidTodoDataError(f"Invalid JSON in {file_path}") from e

    if not isinstance(data, list):
        raise InvalidTodoDataError("Todo data must be a list")

    return data


def save_tasks(file_path: str, tasks: list[Task]) -> None:
    p = Path(file_path)
    p.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def add_task(tasks: list[Task], title: str) -> None:
    tasks.append({"title": title, "done": False})


def finish_task(tasks: list[Task], index: int) -> bool:
    if index < 1 or index > len(tasks):
        return False
    tasks[index - 1]["done"] = True
    return True
