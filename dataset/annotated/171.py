from typing import List, Tuple, Generator

def generate_adjacent_coordinates(ele: List[int], sub: List[int] = []) -> Generator[List[int], None, None]:
    if not ele:
        yield sub
    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                    for idx in generate_adjacent_coordinates(ele[1:], sub + [j])]

def get_coordinates(test_tup: Tuple[int, ...]) -> List[List[int]]:
    return list(generate_adjacent_coordinates(list(test_tup)))

