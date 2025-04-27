def solution(k):
    return next(chr(97 + i) for i, d in enumerate(f'{k:b}'[::-1]) if d == '1')

