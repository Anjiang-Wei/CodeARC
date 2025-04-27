def calculate_permutations(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == n:
        return 1
    if k == 0:
        def subf(n: int) -> int:
            # Base case for recursion
            if n == 0:
                return 1
            # Recursive calculation with alternating sign
            return n * subf(n - 1) + (-1)**n
        return subf(n)
    # Recursive calculation for permutations with one fixed point
    return calculate_permutations(n-1, k-1) * n // k

