def solution(a, b, c):
    x, y, z = sorted([a, b, c])
    # Check if the sides can form a triangle
    if z >= x + y:
        return 0  # Not a triangle
    # Check for a right triangle
    if z * z == x * x + y * y:
        return 2  # Right triangle
    # Check for an acute or obtuse triangle
    return 1 if z * z < x * x + y * y else 3  # Acute or Obtuse triangle

