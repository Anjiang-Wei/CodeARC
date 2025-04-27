def can_john_tell_truth(a: int, b: int, s: int) -> bool:
    delta = abs(a) + abs(b) - s
    # John tells the truth if delta is non-positive and even
    return delta <= 0 and delta % 2 == 0

