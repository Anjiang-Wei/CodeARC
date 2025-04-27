def solution(stations):
    riders, travelled = 1, 0
    
    for dist in stations:
        if travelled + dist > 100:
            riders += 1
            travelled = dist
        else:
            travelled += dist
    
    return riders

