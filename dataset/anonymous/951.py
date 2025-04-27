def solution(a, b):
    # Find common characters in both strings
    common_chars = set(a) & set(b)
    # Concatenate characters from both strings that are not common
    return ''.join(c for c in a + b if c not in common_chars)

