def solution(initVal, patternL, nthTerm):
    from itertools import cycle

    # Iterate over the pattern cyclically
    for c, i in enumerate(cycle(patternL), 2):
        initVal += i
        
        # Check if the current term is the nth term
        if c == nthTerm:
            # Return the sum of the digits of the nth term
            return sum(int(v) for v in str(initVal))

