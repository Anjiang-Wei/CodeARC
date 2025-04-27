def calculate_animals(heads: int, legs: int) -> tuple[int, int] | str:
    chickens, cows = 2 * heads - legs / 2, legs / 2 - heads
    # Check for invalid cases
    if chickens < 0 or cows < 0 or not chickens == int(chickens) or not cows == int(cows):
        return "No solutions"
    # Return the number of chickens and cows as a tuple
    return int(chickens), int(cows)

