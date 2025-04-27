def breakeven_visits(card: float, ticket: float, perc: float) -> int:
    import math
    
    num = 0
    priceA = 0
    priceB = card
    
    while math.ceil(priceB) >= priceA:
        num += 1
        priceA += ticket
        priceB += ticket * (perc ** num)
    
    return num

