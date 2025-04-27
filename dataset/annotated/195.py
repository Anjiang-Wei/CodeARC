from itertools import combinations
from typing import List, Tuple

def calculate_pairwise_sums(test_list: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return [tuple(map(sum, zip(*t))) for t in combinations(test_list, 2)]

