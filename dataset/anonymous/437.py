def solution(s):
    r, rm = [], []
    for i, x in enumerate(s):
        if x in r or len(set(r)) < 2:
            r += x
        else:
            if len(r) > len(rm):
                rm = r[:]
            # Retain the last character(s) that are the same as the last character
            r = [y for y in r[-1::-1] if y == r[-1]] + [x]
    if len(r) > len(rm):
        rm = r[:]
    return ''.join(rm)

