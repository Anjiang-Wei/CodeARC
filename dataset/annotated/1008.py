from typing import List

def max_profit_with_fee(prices: List[int]) -> int:
    m = best = float('-inf')
    for v in reversed(prices):
        m, best = max(m, best - v), max(best, v)
    return m

