from utils import normalize_name, is_valid_phone


def test_normalize_name():
    assert normalize_name("  alice   bob ") == "Alice Bob"


def test_valid_phone_true():
    assert is_valid_phone("13800138000") is True


def test_valid_phone_false():
    assert is_valid_phone("12ab") is False
