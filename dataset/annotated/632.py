def mirror_rot13_cipher(text: str) -> str:
    def encrypt_char(c: str) -> str:
        # If the character is a space, return it as is
        if c == ' ':
            return c
        # Calculate the ROT13 and then find the opposite character
        return chr(122 - ((ord(c) - 97) + 13) % 26)
    
    # Apply the encryption to each character in the string
    return ''.join(encrypt_char(c) for c in text)

