from typing import List

def generate_multiples(limit: int, factor: int) -> List[int]:
    return [i * factor for i in range(1, limit + 1)]

