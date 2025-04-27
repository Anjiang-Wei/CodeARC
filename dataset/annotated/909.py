def is_prime(n: int) -> bool:
    import math
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))

