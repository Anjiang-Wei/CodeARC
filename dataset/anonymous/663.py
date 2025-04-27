def solution(n1, n2):
    from math import log
    
    # Calculate the logarithmic comparison values
    a = n1[1] * log(n1[0])
    b = n2[1] * log(n2[0])
    
    # Return -1 if a > b, 0 if a == b, 1 if a < b
    return (a < b) - (a > b)

