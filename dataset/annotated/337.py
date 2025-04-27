def redistribute_population(population: list[int], minimum: int) -> list[int]:
    if minimum > sum(population) // len(population):
        return []
    
    while min(population) < minimum:
        # Find the index of the poorest and richest
        poorest_index = population.index(min(population))
        richest_index = population.index(max(population))
        
        # Redistribute wealth
        population[poorest_index] += 1
        population[richest_index] -= 1
    
    return population

