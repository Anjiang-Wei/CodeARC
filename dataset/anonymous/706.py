def solution(tape, array):
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

