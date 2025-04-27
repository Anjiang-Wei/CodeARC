from typing import Tuple, Any

def all_elements_same_type(test_tuple: Tuple[Any, ...]) -> bool:
    return all(isinstance(item, type(test_tuple[0])) for item in test_tuple)

