def solution(code, key):
    from itertools import cycle
    from string import ascii_lowercase
    
    keys = cycle(map(int, str(key)))
    # Decode each number by subtracting the corresponding key digit and converting to a letter
    return ''.join(ascii_lowercase[n - next(keys) - 1] for n in code)

