def can_swap_to_equal(A: str, B: str) -> bool:
    from collections import Counter

    if len(A) != len(B):
        return False
    if len(A) < 2:
        return False
    if A == B:
        cnt = Counter(A)
        # Check if there is any character with a frequency greater than 1
        return any(v > 1 for v in cnt.values())
    
    diffs = []
    for i, a in enumerate(A):
        if a != B[i]:
            diffs.append(i)
    
    if len(diffs) == 2:
        i, j = diffs
        # Check if swapping the two differing characters makes the strings equal
        return A[i] == B[j] and A[j] == B[i]
    
    return False

