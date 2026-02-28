from input_guard import divide_from_text


def test_divide_ok():
    assert divide_from_text("10", "2") == 5.0


def test_divide_zero():
    assert divide_from_text("10", "0") == "计算错误：除数不能为0"


def test_divide_bad_input():
    assert divide_from_text("abc", "2") == "输入错误：请输入数字"