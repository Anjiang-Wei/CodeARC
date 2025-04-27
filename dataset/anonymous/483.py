def solution(stations, stationX):
    # Adjust the stations list to account for the missing rider
    stations = stations[:stationX-1] + stations[stationX:]
    rider, dist = 1, 0
    
    for i, d in enumerate(stations):
        # Increment rider count if the distance exceeds 100 miles or if it's the station before the missing rider
        rider += (dist + d > 100) + (i == stationX-2)
        # Update the distance, reset if it exceeds 100 miles or if it's the station before the missing rider
        dist = dist * (dist + d <= 100 and i != stationX-2) + d
    
    return rider

