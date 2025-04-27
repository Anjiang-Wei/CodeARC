def insert_space_before_vowels(s: str) -> str:
    from re import sub
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = sub(r'[^a-z0-9]', '', s.lower())
    # Insert space before each vowel that is not at the start
    result = sub(r'(?<=.)([aeiou])', r' \1', cleaned)
    return result

