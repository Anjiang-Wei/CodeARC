def have_same_characters(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    >>> have_same_characters('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> have_same_characters('abcd', 'dddddddabc')
    True
    >>> have_same_characters('dddddddabc', 'abcd')
    True
    >>> have_same_characters('eabcd', 'dddddddabc')
    False
    >>> have_same_characters('abcd', 'dddddddabce')
    False
    >>> have_same_characters('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    return set(s0) == set(s1)

