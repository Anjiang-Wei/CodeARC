def solution(input):
    vowels = set('aeiouAEIOU')
    s = t = 0
    for c, e in enumerate(input, 1):
        if e in vowels:
            t += c
        s += t
    return s

