def solution(hp, dps, shots, regen):
    from math import ceil
    
    # Check if Megamind can defeat Hal in one full round of shots
    if dps * shots >= hp:
        return ceil(hp / dps)
    
    # Check if Hal's regeneration is too strong to overcome
    if dps * shots <= regen:
        return -1

    # Calculate the number of regeneration periods needed
    number_of_regenerations = ceil((hp - dps * shots) / (dps * shots - regen))
    
    # Calculate the total number of shots needed
    return ceil((hp + regen * number_of_regenerations) / dps)

