def solution(num):
    from itertools import combinations
    
    # Convert the number to a string, then to individual digits
    digits = map(int, str(num))
    
    # Generate all combinations of two digits and calculate their sums
    result = list(map(sum, combinations(digits, 2)))
    
    return result

