def determine_final_direction(n: int, m: int) -> str:
    # Determine the final direction based on the grid dimensions
    return "LR"[n % 2] if m >= n else "UD"[m % 2]

