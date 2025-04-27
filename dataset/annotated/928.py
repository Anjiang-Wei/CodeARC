def convert_to_love_pattern(string: str) -> str:
    return "".join("LOVE"[(ord(c) - 97) % 4] if c.isalpha() else c for c in string)

