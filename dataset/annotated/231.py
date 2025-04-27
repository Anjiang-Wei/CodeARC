def count_bee_occurrences(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    # Transpose the grid to get vertical lines
    v = list(zip(*grid))
    
    # Create padding for diagonal transformations
    b = [None] * len(grid)
    
    # Forward diagonal transformation
    sf = (b[i:] + list(l) + b[:i] for i, l in enumerate(grid))
    
    # Backward diagonal transformation
    sb = (b[:i] + list(l) + b[i:] for i, l in enumerate(grid))
    
    # Filter out None values and create diagonal lines
    df = [[n for n in l if n is not None] for l in zip(*sf)]
    db = [[n for n in l if n is not None] for l in zip(*sb)]
    
    # Combine all lines into a single string
    inline = '\n'.join(map(''.join, grid + v + df + db))
    
    # Count occurrences of 'bee' in all directions
    return (inline + inline[::-1]).count('bee')

