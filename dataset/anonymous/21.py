def solution(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> solution([1, 2, 4, 10], 100)
    True
    >>> solution([1, 20, 4, 10], 5)
    False
    """
    return all(x < t for x in l)

