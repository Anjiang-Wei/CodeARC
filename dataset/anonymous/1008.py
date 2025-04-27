def solution(prices):
    m = best = float('-inf')
    for v in reversed(prices):
        m, best = max(m, best - v), max(best, v)
    return m

