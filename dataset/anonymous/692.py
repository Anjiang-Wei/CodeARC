def solution(s1, s2):
    # Check if the first and last characters are the same and the length modulo 9 is the same
    return (s1[0], s1[-1], len(s1) % 9) == (s2[0], s2[-1], len(s2) % 9)

