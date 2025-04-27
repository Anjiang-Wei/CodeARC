def sort_alphabetic_chars(s: str) -> str:
    """
    Filter out non-alphabetic characters and sort the remaining characters
    in a case-insensitive manner, then join them into a single string.
    
    :param s: Input string
    :return: String with sorted alphabetic characters
    """
    return "".join(sorted(filter(str.isalpha, s), key=str.lower))

