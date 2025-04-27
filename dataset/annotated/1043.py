from typing import List

def generate_unique_permutations(array: List[str]) -> List[str]:
    from itertools import permutations

    def remove_duplicate(old_list: List[str]) -> List[str]:
        final_list = []
        for num in old_list:
            if num not in final_list:
                final_list.append(num)
        return final_list

    array = remove_duplicate(array)
    return [' '.join(element) for element in list(permutations(array, len(array)))]

