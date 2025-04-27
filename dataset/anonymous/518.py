def solution(dividend, divisor):
    while divisor <= dividend:
        dividend = dividend - divisor
    return dividend

