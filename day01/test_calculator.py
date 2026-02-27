from calculator import calculate


def test_add():
    assert calculate(1, "+", 2) == 3


def test_div_zero():
    assert calculate(10, "/", 0) == "错误：除数不能为0"

"""
from calculator import calculate：导入你写的计算函数。
test_add()：验证加法逻辑是否正确，1 + 2 应该等于 3。
test_div_zero()：验证除零保护是否生效，期望返回错误提示文本。
assert：断言，左边结果和右边期望相同才算测试通过。
函数名以 test_ 开头：pytest 才会自动识别并执行。
"""