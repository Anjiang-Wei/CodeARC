def sum_uppercase_ascii(s: str) -> int:
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        sum_uppercase_ascii("") => 0
        sum_uppercase_ascii("abAB") => 131
        sum_uppercase_ascii("abcCd") => 67
        sum_uppercase_ascii("helloE") => 69
        sum_uppercase_ascii("woArBld") => 131
        sum_uppercase_ascii("aAaaaXa") => 153
    """
    return sum([ord(ch) for ch in s if ch.isupper()])

