def calculate_pyramid_blocks(w: int, l: int, h: int) -> int:
    # Calculate the total number of blocks in the pyramid
    return w * l * h + (w + l) * h * (h - 1) // 2 + h * (h - 1) * (2 * h - 1) // 6

