def solution(n, guess):
    """Integer Square Root of an Integer using Hero's method"""
    x = guess
    cnt = 1
    while True:
        newx = (x + n // x) // 2
        if abs(x - newx) < 1:
            return cnt
        x = newx
        cnt += 1

