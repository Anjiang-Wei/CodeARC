def solution(inp):
    from operator import mul
    from math import factorial
    from functools import reduce
    from collections import Counter
    
    # Convert input to string to handle both numbers and strings uniformly
    input_str = str(inp)
    
    # Calculate the total number of permutations
    total_permutations = factorial(len(input_str))
    
    # Calculate the product of factorials of the counts of each unique element
    divisor = reduce(mul, map(factorial, Counter(input_str).values()), 1)
    
    # Return the number of unique permutations
    return total_permutations // divisor

