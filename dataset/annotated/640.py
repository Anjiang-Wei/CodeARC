def can_reach_pump(distance_to_pump: float, mpg: float, fuel_left: float) -> bool:
    # Calculate if the remaining fuel is enough to reach the pump
    return fuel_left >= distance_to_pump / mpg

