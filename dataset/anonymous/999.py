def solution(n):
    if n == 1:
        return 0
    
    # Calculate the ring number
    r = 0 - (1 - n ** 0.5) // 2
    
    # Calculate the distance and modulus
    d, m = divmod(n - (2 * r - 1) ** 2 - 1, 2 * r)
    
    # Calculate the complex number position
    z = (r * (1 + 1j) - m - 1) * 1j ** d
    
    # Return the Manhattan distance
    return abs(z.real) + abs(z.imag)

