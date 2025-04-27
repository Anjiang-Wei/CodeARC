def all_below_threshold(numbers: list[int], threshold: int) -> bool:
    """Return True if all numbers in the list are below the given threshold.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(x < threshold for x in numbers)

