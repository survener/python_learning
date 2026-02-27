def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "错误：除数不能为0"
        return a / b
    return "错误：不支持的运算符"


if __name__ == "__main__":
    try:
        a = float(input("请输入第一个数字: "))
        op = input("请输入运算符(+ - * /): ").strip()
        b = float(input("请输入第二个数字: "))
        print("结果:", calculate(a, op, b))
    except ValueError:
        print("错误：请输入有效数字")