def encrypt_message(message: str, key: int) -> list[int]:
    from itertools import cycle
    # Convert each character to its corresponding number and add the key
    return [ord(a) - 96 + int(b) for a, b in zip(message, cycle(str(key)))]

