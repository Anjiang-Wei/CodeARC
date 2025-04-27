def solution(codes):
    colors = {
        (1, 0, 0): 'red',
        (0, 1, 0): 'green',
        (0, 0, 1): 'blue',
        (1, 0, 1): 'magenta',
        (1, 1, 0): 'yellow',
        (0, 1, 1): 'cyan',
        (1, 1, 1): 'white',
    }
    
    # Default to '0 0 0' if codes is empty
    codes = codes or '0 0 0'
    
    # Convert the string codes to a list of integers
    items = [int(c) for c in codes.split()]
    
    # Find the maximum value in the list
    m = max(items)
    
    # Return the corresponding color or 'black' if all are zero
    return colors[tuple(i == m for i in items)] if m else 'black'

