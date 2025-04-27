def select_based_on_prime(n: int, x: int, y: int) -> int:
    """Returns the value of x if n is a prime number, else returns the value of y.

    Examples:
    select_based_on_prime(7, 34, 12) == 34
    select_based_on_prime(15, 8, 5) == 5
    """
    
    def is_prime(a: int) -> bool:
        return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))
    
    return x if is_prime(n) else y

