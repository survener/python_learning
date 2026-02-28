from pathlib import Path
from clean_log import clean_line, clean_log_file


def test_clean_line():
    assert clean_line("  ERROR   User Login Failed  ") == "error user login failed"


def test_clean_log_file(tmp_path):
    src = tmp_path / "in.log"
    dst = tmp_path / "out.log"

    src.write_text("  A   B  \n\nC   D\n", encoding="utf-8")
    count = clean_log_file(str(src), str(dst))

    assert count == 2
    assert dst.read_text(encoding="utf-8") == "a b\nc d\n"


def test_input_not_found(tmp_path):
    missing = tmp_path / "missing.log"
    out = tmp_path / "out.log"

    try:
        clean_log_file(str(missing), str(out))
        assert False, "应该抛出 FileNotFoundError"
    except FileNotFoundError:
        assert True