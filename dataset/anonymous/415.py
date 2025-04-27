def solution(arr, n):
    from itertools import combinations
    
    # Generate all unique combinations of n elements from the array
    combos = sorted(sorted(c) for c in combinations(set(arr), n) if sum(c) == 0)
    
    # Return the appropriate result based on the number of valid combinations found
    return combos if len(combos) > 1 else combos[0] if combos else "No combinations" if arr else "No elements to combine"

