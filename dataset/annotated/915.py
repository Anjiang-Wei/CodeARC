def convert_alpha_to_binary(s: str) -> str:
    return ''.join(str(1 - ord(c) % 2) if c.isalpha() else c for c in s)

