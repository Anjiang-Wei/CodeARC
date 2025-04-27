def count_even_xor_pairs(A: list[int]) -> int:
    if len(A) < 2:
        return 0
    return sum((a ^ b) % 2 == 0 for i, a in enumerate(A) for b in A[i + 1:])

