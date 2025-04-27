def solution(s):
    a = iter(sorted((c for c in s if c.isalpha()), key=str.lower))
    # Iterate over the string, replacing alphabetic characters with sorted ones
    return ''.join(next(a) if c.isalpha() else c for c in s)

