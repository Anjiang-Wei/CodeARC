from typing import List

def calculate_fit_index(sizes: List[int], hd: int) -> int:
    for i, s in enumerate(sizes):
        if hd < s:
            return i
        hd -= s
    return len(sizes)

