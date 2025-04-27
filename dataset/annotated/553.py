from typing import List, Optional, Union

def sum_of_cubes_for_odds(arr: List[Union[int, float]]) -> Optional[int]:
    # Check if all elements are integers
    if all(type(n) == int for n in arr):
        # Calculate the sum of cubes of odd numbers
        return sum(n**3 for n in arr if n % 2)
    else:
        # Return None if any element is not an integer
        return None

