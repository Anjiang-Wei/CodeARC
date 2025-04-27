def solution(code):
    def translate_char(c):
        # Define the translation mappings
        vowels = 'aiyeou'
        consonants = 'bkxznhdcwgpvjqtsrlmf'
        
        # Preserve case by checking if the character is uppercase
        if c.islower():
            if c in vowels:
                return vowels[(vowels.index(c) + 3) % len(vowels)]
            elif c in consonants:
                return consonants[(consonants.index(c) + 10) % len(consonants)]
        elif c.isupper():
            if c.lower() in vowels:
                return vowels[(vowels.index(c.lower()) + 3) % len(vowels)].upper()
            elif c.lower() in consonants:
                return consonants[(consonants.index(c.lower()) + 10) % len(consonants)].upper()
        
        # Return the character unchanged if it's not a letter
        return c

    # Translate each character in the input string
    return ''.join(translate_char(c) for c in code)

