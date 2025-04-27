from typing import List

def filter_divisible_numbers(numbers: List[int], divisor: int) -> List[int]:
    return [x for x in numbers if x % divisor == 0]

