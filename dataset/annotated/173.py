import heapq as hq
from typing import List, Any

def heap_sort_numbers(iterable: List[Any]) -> List[Any]:
    hq.heapify(iterable)
    return [hq.heappop(iterable) for _ in range(len(iterable))]

