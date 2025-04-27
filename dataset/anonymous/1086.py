def solution(width, height, xs, ys):
    # Check if there are no supply points
    if not xs:
        return [[None for _ in range(width)] for _ in range(height)]
    
    # Calculate the Manhattan distance for each cell from the nearest supply point
    return [
        [
            min(abs(x - x2) + abs(y - ys[i]) for i, x2 in enumerate(xs))
            for x in range(width)
        ]
        for y in range(height)
    ]

