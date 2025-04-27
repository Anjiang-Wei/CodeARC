def remove_vowels_from_string(s: str) -> str:
    import string
    # Create a translation table to remove vowels
    remove_vowels = str.maketrans('', '', 'aeiou')
    # Return the string with vowels removed
    return s.translate(remove_vowels)

