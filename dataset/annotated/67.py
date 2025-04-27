def find_largest_disorder_index(arr: list[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    find_largest_disorder_index([1,2,4,3,5]) = 3
    find_largest_disorder_index([1,2,3]) = -1
    """

    for i in range(len(arr) - 1, 0, -1):
        if not (arr[i] >= arr[i - 1]):
            return i
    return -1

