def sum_of_digit_permutations(n: int) -> int:
    from math import factorial as fact
    
    s = str(n)
    perms = fact(len(s) - 1)
    coefAll = int('1' * len(s))
    
    # Calculate the sum of all permutations
    return coefAll * perms * sum(map(int, s))

