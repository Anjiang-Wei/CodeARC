def shift_encode(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def main() -> tuple[str, str]:
    s = "example"
    encoded = shift_encode(s)
    decoded = "".join([chr((ord(ch) - ord("a") - 5 + 26) % 26 + ord("a")) for ch in encoded])
    return encoded, decoded

