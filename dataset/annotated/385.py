from typing import List, Optional

def product_of_numbers(numbers: List[int]) -> Optional[int]:
    from functools import reduce
    from operator import mul
    return reduce(mul, numbers) if numbers else None

