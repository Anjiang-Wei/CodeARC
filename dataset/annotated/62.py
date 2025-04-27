def check_sorted_with_limited_duplicates(lst: list[int]) -> bool:
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    check_sorted_with_limited_duplicates([5]) ➞ True
    check_sorted_with_limited_duplicates([1, 2, 3, 4, 5]) ➞ True
    check_sorted_with_limited_duplicates([1, 3, 2, 4, 5]) ➞ False
    check_sorted_with_limited_duplicates([1, 2, 3, 4, 5, 6]) ➞ True
    check_sorted_with_limited_duplicates([1, 2, 3, 4, 5, 6, 7]) ➞ True
    check_sorted_with_limited_duplicates([1, 3, 2, 4, 5, 6, 7]) ➞ False
    check_sorted_with_limited_duplicates([1, 2, 2, 3, 3, 4]) ➞ True
    check_sorted_with_limited_duplicates([1, 2, 2, 2, 3, 4]) ➞ False
    '''

    count = dict()
    for x in lst:
        if x not in count: count[x] = 0
        count[x] += 1
        if count[x] > 2: return False
    return lst == sorted(lst)

