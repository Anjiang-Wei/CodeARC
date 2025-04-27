def solution(n):
    if not isinstance(n, int) or n < 1:
        return float("NaN")
    
    i, l = 1, 11
    while l <= n:
        i += 1
        l += 9 * (i + 1) * 10**i
    
    # Calculate the nth digit
    return ((n - l) // (i * 10**(i - 1 - (n - l) % i))) % 10

