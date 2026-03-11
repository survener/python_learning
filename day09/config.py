import json
from pathlib import Path


def load_storage_path(config_path: str, default_path: str = "todo.json") -> str:
    p = Path(config_path)
    if not p.exists():
        return default_path

    text = p.read_text(encoding="utf-8").strip()
    if not text:
        return default_path

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return default_path

    if not isinstance(data, dict):
        return default_path

    value = data.get("storage_path")
    if isinstance(value, str) and value.strip():
        return value.strip()

    return default_path
