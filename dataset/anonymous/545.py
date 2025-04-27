def solution(lower_limit, k):
    from itertools import count, permutations

    for n in count(int(lower_limit**0.5) + 1):
        s = str(n**2)
        if '0' not in s:
            # Generate all permutations of the digits and check if they are perfect squares
            sq_set = {x for x in (int(''.join(p)) for p in permutations(s)) if (x**0.5).is_integer()}
            # Check if the number of perfect squares is equal to k
            if len(sq_set) == k:
                # Return the maximum perfect square from the set
                return max(sq_set)

