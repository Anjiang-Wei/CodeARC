def solution(l: list):
    """Return only positive numbers in the list.
    >>> solution([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> solution([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return list(filter(lambda x: x > 0, l))

