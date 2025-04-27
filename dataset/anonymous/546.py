def solution(s1, s2):
    # Return a list of indices where the characters in the two strings differ
    return [i for i in range(len(s1)) if s1[i] != s2[i]]

