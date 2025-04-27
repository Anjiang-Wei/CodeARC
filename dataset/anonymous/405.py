def solution(string, delimiter=None):
    import re
    
    if delimiter == '':
        raise ValueError('empty delimiter')
    
    if delimiter is None:
        delimiter = r'\s+'
    else:
        delimiter = re.escape(delimiter)
    
    pos = 0
    for m in re.finditer(delimiter, string):
        yield string[pos:m.start()]
        pos = m.end()
    yield string[pos:]

