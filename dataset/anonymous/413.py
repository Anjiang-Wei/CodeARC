def solution(s):
    seen = set(s)
    return ''.join(a for a in s if a.swapcase() in seen)

