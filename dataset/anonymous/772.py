def solution(n, p):
    if p <= 1:
        return None  # Return None if p is less than or equal to 1
    x = 0
    while n % p == 0:
        x += 1
        n //= p
    return x

