def solution(x, y, z):
    # Calculate the total number of subcuboids
    return x * y * z * (x + 1) * (y + 1) * (z + 1) // 8

