def rotate_encrypt(s: str) -> str:
    """Encrypt the input string by rotating the alphabet.
    
    The letters are shifted down by four places.
    For example:
    rotate_encrypt('hi') returns 'lm'
    rotate_encrypt('asdfghjkl') returns 'ewhjklnop'
    rotate_encrypt('gf') returns 'kj'
    rotate_encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    return "".join(map(lambda ch: chr((ord(ch) - ord("a") + 4) % 26 + ord("a")) if ch in d else ch, s))

