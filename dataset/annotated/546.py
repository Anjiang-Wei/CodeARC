def find_difference_indices(s1: str, s2: str) -> list[int]:
    # Return a list of indices where the characters in the two strings differ
    return [i for i in range(len(s1)) if s1[i] != s2[i]]

