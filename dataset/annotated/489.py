from typing import List

def compute_special_sum(a: List[float]) -> float:
    return sum(
        x**(1 + (x >= 0)) * (1 + 2 * (not i % 3)) * (-1) ** (not i % 5)
        for i, x in enumerate(a, 1)
    )

