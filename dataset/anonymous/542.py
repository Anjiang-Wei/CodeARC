def solution(water, clothes, load):
    if load > 2 * clothes:
        return "Too much clothes"

    if load < clothes:
        return "Not enough clothes"

    # Calculate the additional water needed for extra clothes
    for _ in range(load - clothes):
        water *= 1.1

    # Return the water rounded to 2 decimal places
    return round(water, 2)

