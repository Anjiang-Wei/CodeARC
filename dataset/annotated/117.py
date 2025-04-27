from typing import List, Any

def are_all_elements_equal(list1: List[Any], element: Any) -> bool:
    return all(v == element for v in list1)

