def solution(t, k, ls):
    import itertools
    
    # Generate all combinations of k towns
    combinations = itertools.combinations(ls, k)
    
    # Calculate the sum of each combination and filter those within the limit t
    valid_sums = (sum(comb) for comb in combinations if sum(comb) <= t)
    
    # Return the maximum valid sum or None if no valid sum exists
    return max(valid_sums, default=None)

