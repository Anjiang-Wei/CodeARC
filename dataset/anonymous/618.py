def solution(s):
    # Check if there is at least one 'n' in the first string and 'B' in the same position in the second string
    return ('n', 'B') in zip(*s)

