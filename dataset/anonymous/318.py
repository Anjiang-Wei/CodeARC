def solution(s):
    import re
    # Check for any 'g' that is not immediately followed or preceded by another 'g'
    return not re.search(r'(?<!g)g(?!g)', s)

