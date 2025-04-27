def get_sorted_unique_elements(l: list) -> list:
    """Return sorted unique elements in a list
    >>> get_sorted_unique_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

