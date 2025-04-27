def solution(h):
    if not h:
        return 0

    # Transpose the grid to get vertical lines
    v = list(zip(*h))
    
    # Create padding for diagonal transformations
    b = [None] * len(h)
    
    # Forward diagonal transformation
    sf = (b[i:] + list(l) + b[:i] for i, l in enumerate(h))
    
    # Backward diagonal transformation
    sb = (b[:i] + list(l) + b[i:] for i, l in enumerate(h))
    
    # Filter out None values and create diagonal lines
    df = [[n for n in l if n is not None] for l in zip(*sf)]
    db = [[n for n in l if n is not None] for l in zip(*sb)]
    
    # Combine all lines into a single string
    inline = '\n'.join(map(''.join, h + v + df + db))
    
    # Count occurrences of 'bee' in all directions
    return (inline + inline[::-1]).count('bee')

