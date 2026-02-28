def classify_number(n: int) -> str:
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"