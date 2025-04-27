from typing import List, Union

def sum_to_binary_string(arr: List[Union[int, float]]) -> Union[str, bool]:
    for x in arr:
        if type(x) != int:
            return False
    return '{0:b}'.format(sum(arr))

