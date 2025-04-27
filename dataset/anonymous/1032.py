def solution(sizes, hd):
    for i, s in enumerate(sizes):
        if hd < s:
            return i
        hd -= s
    return len(sizes)

