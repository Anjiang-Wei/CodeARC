def find_largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> find_largest_prime_factor(13195)
    29
    >>> find_largest_prime_factor(2048)
    2
    """

    isprime = [True] * (n + 1)
    for i in range(2, n + 1):
        if isprime[i]:
            for j in range(i + i, n + 1, i):
                isprime[j] = False
    for i in range(n - 1, 1, -1):
        if isprime[i] and n % i == 0:
            return i

