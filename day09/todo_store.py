import json
import logging
from pathlib import Path


Task = dict[str, object]

logger = logging.getLogger(__name__)


class TodoStoreError(Exception):
    pass


class InvalidTodoDataError(TodoStoreError):
    pass


def load_tasks(file_path: str) -> list[Task]:
    p = Path(file_path)
    logger.info("Loading tasks from %s", file_path)

    if not p.exists():
        logger.info("File does not exist, returning empty task list: %s", file_path)
        return []

    text = p.read_text(encoding="utf-8").strip()
    if not text:
        logger.info("File is empty, returning empty task list: %s", file_path)
        return []

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in file: %s", file_path)
        raise InvalidTodoDataError(f"Invalid JSON in {file_path}") from e

    if not isinstance(data, list):
        logger.error("Todo data is not a list: %s", file_path)
        raise InvalidTodoDataError("Todo data must be a list")

    logger.info("Loaded %d tasks from %s", len(data), file_path)
    return data


def save_tasks(file_path: str, tasks: list[Task]) -> None:
    p = Path(file_path)
    p.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("Saved %d tasks to %s", len(tasks), file_path)


def add_task(tasks: list[Task], title: str) -> None:
    tasks.append({"title": title, "done": False})
    logger.info("Added task: %s", title)


def finish_task(tasks: list[Task], index: int) -> bool:
    if index < 1 or index > len(tasks):
        logger.warning("Invalid task index: %d", index)
        return False
    tasks[index - 1]["done"] = True
    logger.info("Marked task %d as done", index)
    return True
