def determine_last_marble_color(b: int, w: int) -> str:
    # If the number of black marbles is odd, the last marble will be black.
    # If the number of black marbles is even, the last marble will be white.
    return 'Black' if b % 2 else 'White'

