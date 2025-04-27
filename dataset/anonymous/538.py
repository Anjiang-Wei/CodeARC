def solution(x, y):
    from math import gcd
    
    # Calculate the greatest common divisor
    common_divisor = gcd(x, y)
    
    # Calculate the number of laps for Bob and Charles
    bob_laps = y // common_divisor
    charles_laps = x // common_divisor
    
    # Return the result as a tuple
    return (bob_laps, charles_laps)

