def get_last_digit(n: int) -> int:
    if n < 0: 
        n = -n
    return n % 10

