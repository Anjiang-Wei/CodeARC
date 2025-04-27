def find_reversible_primes(start: int, stop: int) -> list[int]:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def reverse(n: int) -> int:
        return int(str(n)[::-1])

    primes = []
    for n in range(start, stop + 1):
        rev_n = reverse(n)
        if is_prime(n) and is_prime(rev_n) and n != rev_n:
            primes.append(n)
            # Check if the reversed number is within the range and not already added
            if start <= rev_n <= stop and rev_n not in primes:
                primes.append(rev_n)
    
    return sorted(primes)

