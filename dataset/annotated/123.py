def set_leftmost_unset_bit(n: int) -> int: 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1
        temp >>= 1
    return (n | (1 << pos)) 

