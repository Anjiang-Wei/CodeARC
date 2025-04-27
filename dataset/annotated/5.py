def count_distinct_characters_case_insensitive(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters_case_insensitive('xyzXYZ')
    3
    >>> count_distinct_characters_case_insensitive('Jerry')
    4
    """
    return len(set(string.lower()))

