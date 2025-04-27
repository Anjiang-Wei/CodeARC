def solution(s):
    return next((str(b // 11) for b in (int(str(a) + s) for a in range(1, 11)) if b % 11 == 0), 'impossible')

