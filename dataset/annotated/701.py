def extract_reversed_bits(message: str, code: int) -> str:
    return ''.join(message[-1-i] for i, c in enumerate(bin(code)[::-1]) if c == '1' and i < len(message))[::-1]

