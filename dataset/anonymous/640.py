def solution(distance_to_pump, mpg, fuel_left):
    # Calculate if the remaining fuel is enough to reach the pump
    return fuel_left >= distance_to_pump / mpg

