def normalize_text(text: str) -> str:
    return " ".join(text.strip().split()).lower()


def word_count(text: str) -> int:
    cleaned = normalize_text(text)
    if not cleaned:
        return 0
    return len(cleaned.split(" "))