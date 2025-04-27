def solution(*args):
    from itertools import product
    
    # Generate all possible combinations of digits from the input numbers
    nums = set(
        int(''.join(l)) 
        for l in product(*(str(a) for a in args)) 
        if l[0] != '0'  # Discard numbers with leading zeroes
    )
    
    # If there's only one unique number, return its count and value
    if len(nums) == 1:
        return [1, nums.pop()]
    
    # Return the count, minimum, maximum, and sum of all unique numbers
    return [len(nums), min(nums), max(nums), sum(nums)]

