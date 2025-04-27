def encode_to_numbers(string: str) -> str:
    return ''.join(str(ord(c.lower()) - 96) if c.isalpha() else c for c in string)

