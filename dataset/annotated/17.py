def check_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> check_palindrome('')
    True
    >>> check_palindrome('aba')
    True
    >>> check_palindrome('aaaaa')
    True
    >>> check_palindrome('zbcd')
    False
    """
    return text == text[::-1]

