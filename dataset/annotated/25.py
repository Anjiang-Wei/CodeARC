def is_monotonic(sequence: list[int]) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    >>> is_monotonic([1, 2, 4, 20])
    True
    >>> is_monotonic([1, 20, 4, 10])
    False
    >>> is_monotonic([4, 1, 0, -10])
    True
    """
    
    inc, dec = True, True
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]: inc = False
        if sequence[i] < sequence[i + 1]: dec = False
    return inc or dec

