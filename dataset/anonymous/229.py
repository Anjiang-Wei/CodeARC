def solution(start, finish):
    xs = [0] * 10
    for n in range(start, finish + 1):
        for i in str(n):
            xs[int(i)] += 1
    return xs

