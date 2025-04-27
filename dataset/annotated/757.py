def find_min_divisible_permutation(k: int, *args: int) -> str:
    from itertools import permutations

    # Generate all permutations of the input numbers
    perms = permutations(map(str, args), len(args))
    
    # Filter permutations that are divisible by k
    divisible_by_k = filter(lambda x: int(''.join(x)) % k == 0, perms)
    
    # Try to find the minimum permutation that is divisible by k
    try:
        rearranged = min(divisible_by_k, key=lambda x: int(''.join(x)))
        # Return the formatted result
        return 'Rearrangement: {} generates: {} divisible by {}'.format(', '.join(rearranged), ''.join(rearranged), k)
    except ValueError:
        # If no permutation is found, return this message
        return "There is no possible rearrangement"

