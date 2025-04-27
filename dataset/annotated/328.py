def calculate_total_subcuboids(x: int, y: int, z: int) -> int:
    # Calculate the total number of subcuboids
    return x * y * z * (x + 1) * (y + 1) * (z + 1) // 8

