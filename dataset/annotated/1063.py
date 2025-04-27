def calculate_passenger_overflow(cap: int, on: int, wait: int) -> int:
    # Calculate available space on the bus
    available_space = cap - on
    # Determine how many passengers cannot fit
    cannot_fit = wait - available_space
    # Return 0 if all can fit, otherwise return the number that cannot fit
    return max(0, cannot_fit)

