def solution(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> solution('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> solution('abcd', 'dddddddabc')
    True
    >>> solution('dddddddabc', 'abcd')
    True
    >>> solution('eabcd', 'dddddddabc')
    False
    >>> solution('abcd', 'dddddddabce')
    False
    >>> solution('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    return set(s0) == set(s1)

