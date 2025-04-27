def calculate_final_attack(initial_attack: int, monster_list: list[int]) -> int:
    from functools import reduce
    from math import gcd

    # Calculate the final attack value using reduce
    return reduce(lambda a, b: a + (b if b <= a else gcd(a, b)), monster_list, initial_attack)

