from typing import List, Tuple

def find_max_product_pair(arr: List[int]) -> Tuple[int, int]: 
    pairs = [(a, b) for a in arr for b in arr if a != b]
    return max(pairs, key=lambda x: x[0] * x[1])

