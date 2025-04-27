def find_numbers_with_prime_factors_sum(val: int, nMax: int) -> list[int]:
    def primef(n: int) -> list[int]:
        i = 2
        f = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                f.append(i)
        if n > 1:
            f.append(n)
        return f

    result = []
    for i in range(4, nMax + 1):
        fac = primef(i)
        if len(fac) > 1 and fac[0] + fac[-1] == val:
            result.append(i)
    
    return result

