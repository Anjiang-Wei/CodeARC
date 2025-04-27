from typing import Tuple

def solution(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(a: int) -> bool:
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

    if interval1[0] > interval2[0]: 
        interval1, interval2 = interval2, interval1

    l, r = interval2[0], min(interval1[1], interval2[1])
    
    if r < l:
        return "NO"
    
    return "YES" if is_prime(r - l) else "NO"

