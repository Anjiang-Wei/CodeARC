from typing import List, Any

def group_by_key_threshold(lst: List[Any], key: int = 0) -> List[List[Any]]:
    from itertools import groupby
    # Group the list based on whether elements are less than the key
    return [list(g) for _, g in groupby(lst, lambda a: a < key)]

