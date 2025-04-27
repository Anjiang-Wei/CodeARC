def highest_power_of_2_less_than_or_equal(n: int) -> int: 
    i = 0
    while ((1 << i) <= n): 
        i += 1
    return (1 << (i - 1))

