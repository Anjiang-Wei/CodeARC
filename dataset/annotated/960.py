from typing import List

def sum_of_odd_numbers_with_three(arr: List[int]) -> int:
    # Check if the array is not empty and calculate the sum of odd numbers containing '3'
    return sum(x for x in arr if x % 2 and '3' in str(x)) if arr else 0

