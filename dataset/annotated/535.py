from typing import List

def filter_even_count_numbers(numbers: List[int]) -> List[int]:
    # Create a list comprehension to filter numbers with even counts
    return [i for i in numbers if numbers.count(i) % 2 == 0]

