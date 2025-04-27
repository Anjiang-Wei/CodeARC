def first_non_repeating_character(string: str) -> str:
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
    return ""

