def solution(x, t):
    arr = [x[0]]
    for c in x[1:]:
        if c + arr[-1] != t:
            arr.append(c)
    return arr

