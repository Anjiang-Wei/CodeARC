from typing import List

def is_arithmetic_sequence(seq: List[int]) -> bool:
    return len({a - b for a, b in zip(seq, seq[1:])}) == 1

