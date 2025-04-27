def is_number_simple_power_of_base(x: int, n: int) -> bool:
    """Returns true if a number x is a simple power of n and false otherwise.
    A number x is a simple power of n if n**int = x.
    For example:
    is_number_simple_power_of_base(1, 4) => true
    is_number_simple_power_of_base(2, 2) => true
    is_number_simple_power_of_base(8, 2) => true
    is_number_simple_power_of_base(3, 2) => false
    is_number_simple_power_of_base(3, 1) => false
    is_number_simple_power_of_base(5, 3) => false
    """

    if x == 1: return True
    if n == 0: return x == 0
    if n == 1: return x == 1
    if n == -1: return abs(x) == 1
    p = n
    while abs(p) <= abs(x):
        if p == x: return True
        p = p * n
    return False

