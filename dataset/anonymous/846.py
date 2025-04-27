def solution(a):
    s = set(a)
    # Create pairs (x, x + 2) for each x in a if x + 2 exists in the set
    result = sorted((x, x + 2) for x in a if x + 2 in s)
    return result

