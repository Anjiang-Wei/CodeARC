def ant_simulation(n: int) -> int:
    move = [
        lambda p: (p[0] + 1, p[1]), 
        lambda p: (p[0], p[1] + 1), 
        lambda p: (p[0] - 1, p[1]), 
        lambda p: (p[0], p[1] - 1)
    ]
    start, loop, size = 9977, 104, 12
    pos, d, black, res = (0, 0), 0, set(), 0
    
    if n > start:
        x = (n - start) % loop
        res = size * (n - start - x) // loop
        n = start + x
    
    for i in range(n):
        if pos in black:
            black.remove(pos)
            d = (d + 1) % 4
        else:
            black.add(pos)
            d = (d - 1) % 4
        pos = move[d](pos)
    
    return res + len(black)

