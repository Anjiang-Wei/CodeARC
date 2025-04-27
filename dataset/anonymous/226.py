def solution(s):
    import re
    # Use regex to replace multiple dashes (with or without spaces between) with a single dash
    return re.sub(r'-[ -]+-|-+', r'-', s)

