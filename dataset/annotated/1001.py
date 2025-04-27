def rot13_cipher(message: str) -> str:
    def decode(c: str) -> str:
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    
    return "".join(decode(c) for c in message)

