from typing import List, Union

def filter_out_strings(lst: List[Union[int, float, str]]) -> List[Union[int, float]]:
    # Return a new list with the strings filtered out
    return [i for i in lst if not isinstance(i, str)]

