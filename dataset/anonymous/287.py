def solution(n):
    while n > 9:
        n = bin(n).count("1")
    return n

