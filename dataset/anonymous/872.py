def solution(s):
    from functools import reduce
    from itertools import cycle
    from operator import add, truediv, mul, sub

    # Sort numbers based on the embedded letter
    xs = sorted(s.split(), key=lambda x: next(c for c in x if c.isalpha()))
    
    # Extract digits from each number
    xs = [int(''.join(filter(str.isdigit, x))) for x in xs]
    
    # Define the operation cycle
    ops = cycle([add, sub, mul, truediv])
    
    # Apply operations in sequence and round the result
    return round(reduce(lambda a, b: next(ops)(a, b), xs))

