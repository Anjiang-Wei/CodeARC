def find_combinations_with_sum(a1: list, a2: list, a3: list) -> list:
    return [[x, y, x + y] for x in a1 for y in a2 if x + y in a3]

