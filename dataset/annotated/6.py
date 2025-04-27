def count_overlapping_substring_occurrences(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> count_overlapping_substring_occurrences('', 'a')
    0
    >>> count_overlapping_substring_occurrences('aaa', 'a')
    3
    >>> count_overlapping_substring_occurrences('aaaa', 'aa')
    3
    """

    occurrences = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            occurrences += 1
    return occurrences

