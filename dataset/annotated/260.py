def relatively_prime_numbers(n: int, arr: list[int]) -> list[int]:
    from math import gcd
    # Return numbers in arr that are relatively prime to n
    return [x for x in arr if gcd(n, x) == 1]

