def solution(x, monster_list):
    from functools import reduce
    from math import gcd

    # Calculate the final attack value using reduce
    return reduce(lambda a, b: a + (b if b <= a else gcd(a, b)), monster_list, x)

