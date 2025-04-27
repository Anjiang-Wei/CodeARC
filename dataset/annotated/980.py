def sum_of_unique_permutations(num: int) -> int:
    from itertools import permutations
    
    sNum = str(num)
    # Use a set to avoid duplicate numbers
    unique_numbers = {int(''.join(p)) for d in range(1, len(sNum) + 1) for p in permutations(sNum, d)}
    
    # Return the sum of all unique numbers
    return sum(unique_numbers)

