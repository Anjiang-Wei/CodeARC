def toggle_bits_until_end(tape: str, array: str) -> str:
    from itertools import cycle
    
    idx, result = 0, list(map(int, array))
    
    for cmd in cycle(map(int, tape)):
        if idx == len(array):
            break
        if cmd:
            result[idx] = 1 - result[idx]
        else:
            idx += 1
    
    return ''.join(map(str, result))

