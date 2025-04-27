def count_and_max_divisible_by_three(num: int) -> list[int, int]:
    from itertools import permutations

    num_list = tuple(map(int, str(num)))
    
    poss = set()
    for i in range(1, len(num_list) + 1):
        poss |= set(permutations(num_list, i))
    
    res = set()
    for p in poss:
        if p[0] != 0 and sum(p) % 3 == 0:
            res.add(p)

    # Convert each tuple in res to an integer
    res = [sum(x * 10**n for n, x in enumerate(p[::-1])) for p in res]
    
    # Return the count of multiples and the maximum multiple
    return [len(res), max(res)]

