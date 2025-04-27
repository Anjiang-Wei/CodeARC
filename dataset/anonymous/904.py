def solution(s):
    ds = ""
    for i, d in enumerate(s):
        if d == "|":
            ds += "/"
        else:
            # Reaction stops when a non-standing domino or space is encountered
            return ds + s[i:]
    return ds

