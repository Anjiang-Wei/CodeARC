def calculate_max_levels(bonus: int, price: int) -> int:
    beers = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers -= levels ** 2
    
    return levels

