def normalize_name(name: str) -> str:
    return " ".join(name.strip().split()).title()


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and 6 <= len(phone) <= 15
