def find_greatest_integer_with_frequency(lst: list[int]) -> int:
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        find_greatest_integer_with_frequency([4, 1, 2, 2, 3, 1]) == 2
        find_greatest_integer_with_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        find_greatest_integer_with_frequency([5, 5, 4, 4, 4]) == -1
    '''

    count = dict()
    for num in lst:
        if num not in count:
            count[num] = 0
        count[num] += 1
    ans = -1
    for num, cnt in count.items():
        if cnt >= num:
            ans = max(ans, num)
    return ans

