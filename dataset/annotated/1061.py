def shift_characters(text: str, rule: int) -> str:
    return "".join(chr((ord(i) + rule) % 256) for i in text)

