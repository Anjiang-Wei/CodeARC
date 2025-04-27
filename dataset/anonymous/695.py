def solution(scrapOfTheUsedMachines, numberOfRobotsToProduce):
    from math import ceil
    
    # Initial weight required for one robot
    weight_per_robot = 50
    
    # Adjust weight for each machine's scrap rate
    for scrap in scrapOfTheUsedMachines:
        weight_per_robot /= (1 - scrap / 100)
    
    # Calculate total iron needed and round up to nearest whole number
    total_iron_needed = ceil(numberOfRobotsToProduce * weight_per_robot)
    
    return total_iron_needed

