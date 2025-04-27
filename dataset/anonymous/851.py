def solution(prices: str) -> str:
    from bisect import bisect_left
    from collections import deque

    all_prices = deque(sorted(map(int, prices.split())))  # Ensure sorted order
    discounts = []

    while all_prices:
        d = all_prices.popleft()
        discounts.append(d)

        # Find the corresponding initial price
        target = d * 4 // 3
        index = bisect_left(all_prices, target)

        # Ensure index is within bounds and matches the expected value
        if index < len(all_prices) and all_prices[index] == target:
            del all_prices[index]

    return ' '.join(map(str, discounts))

