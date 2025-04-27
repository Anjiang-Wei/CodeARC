def min_repetitions_to_contain(A: str, B: str) -> int:
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    # Check if all characters in B are in A
    if not set(B).issubset(set(A)):
        return -1
    
    # Calculate the maximum number of repetitions needed
    max_rep = len(B) // len(A) + 3
    A_new = A
    
    # Try to find B as a substring in repeated A
    for i in range(1, max_rep):
        if B in A_new:
            return i
        A_new += A
    
    return -1

