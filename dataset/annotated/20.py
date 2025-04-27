def filter_vowels(text: str) -> str:
    """
    filter_vowels is a function that takes a string and returns a string without vowels.
    >>> filter_vowels('')
    ''
    >>> filter_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> filter_vowels('abcdef')
    'bcdf'
    >>> filter_vowels('aaaaa')
    ''
    >>> filter_vowels('aaBAA')
    'B'
    >>> filter_vowels('zbcd')
    'zbcd'
    """

    return "".join(list(filter(lambda ch: ch not in "aeiouAEIOU", text)))

