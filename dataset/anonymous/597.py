def solution(bonus, price):
    beers = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers -= levels ** 2
    
    return levels

