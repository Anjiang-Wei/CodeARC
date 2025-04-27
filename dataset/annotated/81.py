def cleanse_string_of_chars(string: str, chars_to_remove: str) -> str:
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string

