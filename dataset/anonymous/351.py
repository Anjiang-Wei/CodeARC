def solution(template, data='1234567890'):
    from itertools import cycle
    
    data = cycle(data)
    # Replace alphabetical characters with numbers from the data
    return ''.join(next(data) if c.isalpha() else c for c in template)

