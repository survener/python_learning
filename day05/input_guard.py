def divide_from_text(a_text: str, b_text: str):
    try:
        a = float(a_text)
        b = float(b_text)
    except ValueError:
        return "输入错误：请输入数字"

    if b == 0:
        return "计算错误：除数不能为0"

    return a / b


if __name__ == "__main__":
    a = input("请输入被除数: ").strip()
    b = input("请输入除数: ").strip()
    print("结果:", divide_from_text(a, b))