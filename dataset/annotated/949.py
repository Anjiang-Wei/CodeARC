def calculate_min_riders_required(stations: list[int]) -> int:
    riders, travelled = 1, 0
    
    for dist in stations:
        if travelled + dist > 100:
            riders += 1
            travelled = dist
        else:
            travelled += dist
    
    return riders

