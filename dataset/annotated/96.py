from collections import defaultdict
from typing import List, Any

def find_max_occurrences(nums: List[Any]) -> Any:
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    return max(d, key=d.get)

