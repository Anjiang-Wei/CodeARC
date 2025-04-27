def encrypt_message(code: str, message: str) -> str:
    code, dct = sorted(set(code)), {}
    
    # Create the mapping dictionary
    for c1, c2 in zip(code, code[1:] + [chr(ord("z") + ord(code[0]) - ord("a"))]):
        for n in range(ord(c1), ord(c2) + 1):
            dct[chr((n - 97) % 26 + 97)] = c1 + str(n - ord(c1) + 1)
    
    # Generate the encrypted message
    return ''.join(dct[c] for c in message)

