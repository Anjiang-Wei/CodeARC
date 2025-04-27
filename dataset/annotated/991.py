def sum_of_dominant_primes_within_range(a: int, b: int) -> int:
    def generate_primes_and_dominants(limit: int) -> list[int]:
        # Sieve of Eratosthenes to find all primes up to limit
        sieve, primes = [0] * (limit // 2 + 1), [0, 2]
        for i in range(3, limit + 1, 2):
            if not sieve[i // 2]:
                primes.append(i)
                for j in range(i * i, limit + 1, i * 2):
                    sieve[j // 2] = 1

        # Find dominant primes
        dominants = []
        for p in primes:
            if p >= len(primes):
                break
            dominants.append(primes[p])
        
        return dominants

    # Generate dominants up to 500000
    dominants = generate_primes_and_dominants(500000)

    # Calculate the sum of dominant primes within the range [a, b]
    return sum(p for p in dominants if a <= p <= b)

