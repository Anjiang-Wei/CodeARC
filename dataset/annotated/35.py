def min_changes_to_palindrome(arr: list[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    min_changes_to_palindrome([1,2,3,5,4,7,9,6]) == 4
    min_changes_to_palindrome([1, 2, 3, 4, 3, 2, 2]) == 1
    min_changes_to_palindrome([1, 2, 3, 2, 1]) == 0
    """
    arr_reversed, cnt = arr[::-1], 0
    for i in range(len(arr) // 2):
        if arr[i] != arr_reversed[i]:
            cnt += 1
    return cnt

