from typing import List

def filter_numbers_without_even_digit(numbers: List[int]) -> List[int]:
    """Given a list of positive integers, return a sorted list of all 
    elements that don't have any even digits.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> filter_numbers_without_even_digit([15, 33, 1422, 1])
    [1, 15, 33]
    >>> filter_numbers_without_even_digit([152, 323, 1422, 10])
    []
    """

    def has_no_even_digits(x: int) -> bool:
        for ch in str(x):
            if int(ch) % 2 == 0:
                return False
        return True
        
    return sorted(list(filter(has_no_even_digits, numbers)))

