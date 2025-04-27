def find_prime_gap(g: int, m: int, n: int) -> list:
    import math
    
    def isPrime(num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    if m >= n:
        return []
    
    for i in range(m, n + 1 - g):
        if isPrime(i) and isPrime(i + g):
            return [i, i + g]
    
    return []

