import pytest
from math_tools import classify_number


@pytest.mark.parametrize(
    "value, expected",
    [
        (10, "positive"),
        (1, "positive"),
        (0, "zero"),
        (-1, "negative"),
        (-99, "negative"),
    ],
)
def test_classify_number(value, expected):
    assert classify_number(value) == expected