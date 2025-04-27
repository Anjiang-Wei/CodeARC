def solution(text: str):
    """
    Checks if given string is a palindrome
    >>> solution('')
    True
    >>> solution('aba')
    True
    >>> solution('aaaaa')
    True
    >>> solution('zbcd')
    False
    """

    return text == text[::-1]

