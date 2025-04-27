def round_up_to_nearest_multiple(base: int, number: int) -> int:
    return number + (base - number) % base

