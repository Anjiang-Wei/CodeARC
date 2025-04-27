def filter_positive_numbers(nums: list[int]) -> list[int]:
    """Return only positive numbers in the list.
    >>> filter_positive_numbers([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> filter_positive_numbers([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return list(filter(lambda x: x > 0, nums))

