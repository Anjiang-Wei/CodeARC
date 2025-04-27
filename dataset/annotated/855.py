from typing import List

def can_reach_target_evenly(N: List[int], x: int, y: int) -> bool:
    # Check if the difference between y and x is even
    # or if any knight's n value is even
    return (y - x) % 2 == 0 or any(n % 2 == 0 for n in N)

