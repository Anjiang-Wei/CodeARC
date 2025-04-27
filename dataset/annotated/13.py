def has_triplet_with_zero_sum(nums: list[int]) -> bool:
    """
    has_triplet_with_zero_sum takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> has_triplet_with_zero_sum([1, 3, 5, 0])
    False
    >>> has_triplet_with_zero_sum([1, 3, -2, 1])
    True
    >>> has_triplet_with_zero_sum([1, 2, 3, 7])
    False
    >>> has_triplet_with_zero_sum([2, 4, -5, 3, 9, 7])
    True
    >>> has_triplet_with_zero_sum([1])
    False
    """

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    return True
    return False

