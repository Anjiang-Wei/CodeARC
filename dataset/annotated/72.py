from typing import List

def sort_by_digit_sum(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> sort_by_digit_sum([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> sort_by_digit_sum([]) == []
    """

    def weight(x: int) -> int:
        x_list = list(str(x))
        if x_list[0] == "-":
            x_list = x_list[1:]
            x_list = list(map(int, x_list))
            x_list[0] = -x_list[0]
        else:
            x_list = list(map(int, x_list))
        return sum(x_list)
    return sorted(nums, key=weight)

