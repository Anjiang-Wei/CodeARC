def solution(n):
    # If the name length is greater than 2, return both full and truncated names
    # Otherwise, return the name as is
    return [n, n[:2]] if len(n) > 2 else [n]

