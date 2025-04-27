def remove_digits(s: str) -> str:
    return ''.join(x for x in s if not x.isdigit())

