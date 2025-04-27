from typing import List

def determine_sum_parity(arr: List[int]) -> str:
    # Calculate the sum of the array elements
    # Check if the sum is even or odd
    return 'even' if sum(arr) % 2 == 0 else 'odd'

