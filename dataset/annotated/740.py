def find_floyds_triangle_line(n: int) -> int:
    # Calculate the line number in Floyd's triangle where the number n falls
    return int(((1 + 8 * (n - 1))**0.5 + 1) // 2)

