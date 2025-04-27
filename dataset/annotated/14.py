def has_pair_with_zero_sum(numbers: list[int]) -> bool:
    """
    has_pair_with_zero_sum takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    >>> has_pair_with_zero_sum([1, 3, 5, 0])
    False
    >>> has_pair_with_zero_sum([1, 3, -2, 1])
    False
    >>> has_pair_with_zero_sum([1, 2, 3, 7])
    False
    >>> has_pair_with_zero_sum([2, 4, -5, 3, 5, 7])
    True
    >>> has_pair_with_zero_sum([1])
    False
    """
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == 0:
                return True
    return False

