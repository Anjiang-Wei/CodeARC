def caesar_cipher_encrypt(message: str, key: int) -> str:
    def caeser_cipher(message: str, key: int) -> str:
        # Encrypt each character if it's an alphabet
        return ''.join(
            chr(65 + (ord(c.upper()) + key - 65) % 26) if c.isalpha() else c 
            for c in message
        )
    
    # Return the encrypted message
    return caeser_cipher(message, key)

