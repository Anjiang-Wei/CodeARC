from typing import Tuple

def multiply_adjacent_elements(test_tup: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(i * j for i, j in zip(test_tup, test_tup[1:]))

