from config import load_storage_path


def test_missing_config_returns_default(tmp_path):
    p = tmp_path / "config.json"
    assert load_storage_path(str(p)) == "todo.json"


def test_empty_config_returns_default(tmp_path):
    p = tmp_path / "config.json"
    p.write_text("", encoding="utf-8")
    assert load_storage_path(str(p)) == "todo.json"


def test_invalid_json_returns_default(tmp_path):
    p = tmp_path / "config.json"
    p.write_text("{bad json", encoding="utf-8")
    assert load_storage_path(str(p)) == "todo.json"


def test_valid_config_returns_path(tmp_path):
    p = tmp_path / "config.json"
    p.write_text('{"storage_path": "data/todo.json"}', encoding="utf-8")
    assert load_storage_path(str(p)) == "data/todo.json"
