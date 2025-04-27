def does_ray_exit_corners(max_x: int, max_y: int) -> bool:
    x = y = 0
    dx = dy = 1
    while True:
        x += dx
        y += dy
        # Check if the ray exits at (0, 0) or (max_x, max_y)
        if (x == 0 and y == 0) or (x == max_x and y == max_y):
            return True
        # Check if the ray exits at any other corner
        if (x == 0 or x == max_x) and (y == 0 or y == max_y):
            return False
        # Reflect the ray on the x-axis
        if x in (0, max_x):
            dx *= -1
        # Reflect the ray on the y-axis
        if y in (0, max_y):
            dy *= -1

