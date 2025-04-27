def solution(text, mode='encrypt'):
    region = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&\""

    def encrypt(text):
        if not text:
            return text
        
        if any(c not in region for c in text):
            raise Exception("Character not in region.")

        letters = list(text)
        for i in range(1, len(letters), 2):
            letters[i] = text[i].swapcase()
        
        swapped = letters[:]
        for i in range(1, len(letters)):
            letters[i] = region[(region.index(swapped[i - 1]) - region.index(swapped[i])) % len(region)]
        
        letters[0] = region[-(region.index(swapped[0]) + 1)]
        return "".join(letters)

    def decrypt(encrypted_text):
        if not encrypted_text:
            return encrypted_text
        
        if any(c not in region for c in encrypted_text):
            raise Exception("Character not in region.")

        letters = list(encrypted_text)
        letters[0] = region[-(region.index(letters[0]) + 1)]
        for i in range(1, len(letters)):
            letters[i] = region[(region.index(letters[i - 1]) - region.index(letters[i])) % len(region)]
        
        for i in range(1, len(letters), 2):
            letters[i] = letters[i].swapcase()

        return "".join(letters)

    if mode == 'encrypt':
        return encrypt(text)
    elif mode == 'decrypt':
        return decrypt(text)
    else:
        raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

