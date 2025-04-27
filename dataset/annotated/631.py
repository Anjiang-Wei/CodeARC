from typing import List, Any

def remove_nth_element(a: List[Any], n: int) -> List[Any]:
    # Return the list with the nth element removed
    return a[:n] + a[n+1:]

