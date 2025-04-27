def equalize_candies(candies: list[int]) -> list[int]:
    steps = 0
    while len(set(candies)) > 1:
        # Distribute candies: each child gives half to the right, rounding up if odd
        candies = [(a + 1) // 2 + (b + 1) // 2 for a, b in zip(candies, candies[-1:] + candies)]
        steps += 1
    # Return the number of steps and the final number of candies each child has
    return [steps, candies.pop()]

