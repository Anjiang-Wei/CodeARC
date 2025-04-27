def calculate_days_to_reach_top(column: int, day: int, night: int) -> int:
    from math import ceil
    # Calculate the number of days required for the snail to reach the top
    return max(ceil((column - night) / (day - night)), 1)

