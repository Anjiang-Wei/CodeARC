def solution(l):
    """
    solution takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> solution([1, 3, 5, 0])
    False
    >>> solution([1, 3, -2, 1])
    False
    >>> solution([1, 2, 3, 7])
    False
    >>> solution([2, 4, -5, 3, 5, 7])
    True
    >>> solution([1])
    False
    """
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == 0:
                return True
    return False

