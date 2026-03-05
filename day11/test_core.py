from myapp.core import normalize_text, word_count


def test_normalize_text():
    assert normalize_text("  Hello   WORLD  ") == "hello world"


def test_word_count_normal():
    assert word_count("one two  three") == 3


def test_word_count_empty():
    assert word_count("   ") == 0