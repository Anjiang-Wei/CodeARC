from typing import Tuple

def is_tuple_distinct(test_tup: Tuple) -> bool:
    return len(test_tup) == len(set(test_tup))

