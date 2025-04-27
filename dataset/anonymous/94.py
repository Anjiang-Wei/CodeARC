import math

def solution(a, b): 
    total = 0
    n = math.gcd(a, b)
    N = int(math.sqrt(n)) + 1
    for i in range(1, N): 
        if (n % i == 0): 
            total += i
            if (n // i != i): 
                total += (n // i)
    return total

