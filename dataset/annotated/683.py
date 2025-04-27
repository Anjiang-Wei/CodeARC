def compute_least_common_multiple(n: int, k: int) -> int:
    from collections import Counter
    from math import ceil

    def get_factors(n: int) -> Counter:
        PRIMES = [2] + [num for num in range(3, 1000, 2) if all(num % d for d in range(3, int(num**0.5) + 1, 2))]
        factors = []
        for p in PRIMES:
            if p > n: 
                break
            while n % p == 0:
                factors.append(p)
                n //= p
        if n > 1:
            factors.append(n)
        return Counter(factors)

    factors, lcm = get_factors(n), 1
    for p, e in factors.items():
        lcm *= p**(ceil(e/k)*k)
    return lcm // n

