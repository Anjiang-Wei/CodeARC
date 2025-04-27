from typing import List, Tuple

def find_square_pairs(upper_limit: int, k: int) -> List[Tuple[int, int]]:
    import math

    square_lim = int((2 * upper_limit) ** 0.5) + 1
    squares = [n * n for n in range(1, square_lim)]
    pairs = []
    square_set = set(squares)

    for m in range(upper_limit - 1, 1, -1):
        for b in squares:
            if b >= m:
                break
            if 2 * m - b in square_set:
                pairs.append((m, m - b))
                if len(pairs) == k:
                    return pairs

