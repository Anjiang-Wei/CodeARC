def solution(cons, petrol, dist=None):
    import math

    def total_kilometers(cons, petrol):
        # Calculate total kilometers that can be driven with given petrol and consumption
        return round(100 * petrol / cons, 2)

    def check_distance(dist, cons, petrol):
        # Check if the distance can be covered with the given petrol and consumption
        if dist > total_kilometers(cons, petrol):
            return "You will need to refuel"
        else:
            # Calculate the status after every 100 km
            return [[n * 100, dist - 100 * n, round(petrol - cons * n, 2)] for n in range(dist // 100 + 1)]

    if dist is None:
        # If only consumption and petrol are provided, calculate total kilometers
        return total_kilometers(cons, petrol)
    else:
        # If distance is also provided, check the distance
        return check_distance(dist, cons, petrol)

