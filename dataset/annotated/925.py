def is_not_power_of_two(n: int) -> bool:
    from math import log2
    # Check if n is a power of 2 by verifying if log2(n) is an integer
    return not log2(n).is_integer()

