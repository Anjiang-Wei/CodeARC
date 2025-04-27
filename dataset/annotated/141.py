from typing import List

def generate_combinations(input_list: List) -> List[List]:
    if len(input_list) == 0:
        return [[]]
    result = []
    for el in generate_combinations(input_list[1:]):
        result += [el, el + [input_list[0]]]
    return result

