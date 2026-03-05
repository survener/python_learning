from myapp.core import normalize_text, word_count


def run_demo(text: str) -> str:
    normalized = normalize_text(text)
    count = word_count(text)
    return f"normalized='{normalized}', words={count}"


if __name__ == "__main__":
    user_input = input("Enter text: ")
    print(run_demo(user_input))