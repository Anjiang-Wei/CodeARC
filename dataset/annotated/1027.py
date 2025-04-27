def convert_to_pig_latin(st: str) -> str:
    def pig_latin(s: str) -> str:
        VOWELS = set('aeiou')
        s = s.lower()
        if s.isalpha():
            if set(s) & VOWELS:
                if s[0] in VOWELS:
                    s += 'w'
                while s[0] not in VOWELS:
                    s = s[1:] + s[:1]
            return s + 'ay'
        return None  # Return None if the string contains non-alpha characters

    return pig_latin(st)

