def solution(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> solution([1, 2, 4, 20])
    True
    >>> solution([1, 20, 4, 10])
    False
    >>> solution([4, 1, 0, -10])
    True
    """

    inc, dec = True, True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]: inc = False
        if l[i] < l[i + 1]: dec = False
    return inc or dec

