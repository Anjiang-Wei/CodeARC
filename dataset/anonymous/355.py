def solution(n):
    return [(c == '1') * 2 - 1 for c in '1' + bin(n)[2:-1]]

