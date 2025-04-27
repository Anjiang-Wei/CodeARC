def calculate_black_cells(n: int, m: int) -> int:
    from math import gcd
    # Calculate the number of black cells using the formula
    return (n + m) - 2 + gcd(n, m)

