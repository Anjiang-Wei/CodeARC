def solution(a, b):
    from bisect import bisect_left, bisect

    # Set of odd digits
    ss = set('13579')
    
    # Generate all perfect cubes with odd digits
    ns = [i ** 3 for i in range(1, int((10 ** 17) ** (1/3)) + 3, 2) if set(str(i ** 3)) <= ss]
    
    # Include negative cubes
    ns = [-n for n in ns[::-1]] + ns

    # Return the range of numbers within [a, b]
    return ns[bisect_left(ns, a):bisect(ns, b)]

