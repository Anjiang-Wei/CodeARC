from typing import List

def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [i for i in numbers if i % 2 == 0]

