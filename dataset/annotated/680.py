def calculate_max_profit(prices: list[int]) -> int:
    profits = 0
    ln = len(prices)
    
    if not ln:
        return 0
    elif ln == 2:
        return (prices[1] - prices[0]) if prices[1] > prices[0] else 0
    
    lastPrice = prices[0]
    for price in prices:
        if lastPrice < price:
            profits += (price - lastPrice)
        lastPrice = price
    
    return profits

