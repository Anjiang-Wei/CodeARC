def calculate_permutation_statistics(arr: list[int]) -> list[dict[str, int]]:
    from itertools import permutations
    
    # Generate all unique permutations of the array
    perms = set(permutations(arr))
    
    # Calculate the special score for each permutation
    values = [sum((x + 1) * y for x, y in enumerate(i)) for i in perms]
    
    # Return the required statistics as a list of dictionaries
    return [
        {"total perm": len(perms)},
        {"total ssc": sum(values)},
        {"max ssc": max(values)},
        {"min ssc": min(values)}
    ]

