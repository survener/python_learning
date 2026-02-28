import json
from pathlib import Path


def load_tasks(file_path: str):
    p = Path(file_path)
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)


def save_tasks(file_path: str, tasks):
    p = Path(file_path)
    p.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def add_task(tasks, title: str):
    tasks.append({"title": title, "done": False})


def finish_task(tasks, index: int):
    if index < 1 or index > len(tasks):
        return False
    tasks[index - 1]["done"] = True
    return True