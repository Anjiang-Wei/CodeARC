def solution(n):
    sP, p = set(), 2
    while n > 1 and p <= n**0.5:
        while not n % p:
            if p in sP:
                return 0  # n is divisible by the square of a prime
            sP.add(p)
            n //= p
        p += 1 + (p != 2)
    # Return 1 if even number of prime factors, -1 if odd
    return (-1) ** ((len(sP) + (n != 1)) % 2)

