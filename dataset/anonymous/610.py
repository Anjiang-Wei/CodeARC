def solution(start, k):
    def arith_deriv(n):
        factors = prime_factors(n)
        return sum(n * factors.count(factor) // factor for factor in set(factors)) or 1

    def prime_factors(n):
        if n < 2:
            return []
        factors = []
        for k in (2, 3):
            while n % k == 0:
                n //= k
                factors.append(k)
        k = 5
        step = 2
        while k * k <= n:
            if n % k:
                k += step
                step = 6 - step
            else:
                n //= k
                factors.append(k)
        if n > 1:
            factors.append(n)
        return factors

    if len(prime_factors(start)) < 2:
        return "{} is a prime number".format(start)
    
    chain = [start]
    while k > 1:
        k, start = k-1, arith_deriv(start)
        chain.append(start)
    
    return chain

