def split_string_by_delimiter(string: str, delimiter: str = None) -> 'generator[str, None, None]':
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

