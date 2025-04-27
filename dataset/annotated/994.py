from typing import List, Union

def find_sequences(arr: List[int], command: str) -> Union[List[int], List[List[int]]]:
    from itertools import starmap, combinations
    from operator import lt, gt

    check = lt if command.startswith('<') else gt
    for i in range(len(arr), 2, -1):
        # Generate combinations of length i and check if they are strictly increasing or decreasing
        result = [list(x) for x in combinations(arr, i) if all(starmap(check, zip(x, x[1:])))]
        # Return the result if any valid combination is found
        if result:
            return result[0] if len(result) == 1 else result
    return []

