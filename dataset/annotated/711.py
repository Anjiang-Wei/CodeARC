from typing import List

def find_repeated_subsequence(sequence: List[int]) -> List[int]:
    for j, x in enumerate(sequence):
        i = sequence.index(x)
        if 0 <= i < j:
            return [i, j - i]
    return []

