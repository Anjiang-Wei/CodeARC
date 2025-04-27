def expand_string(s: str) -> str:
    m, n = '', 1
    for j in s:
        if j.isdigit():
            n = int(j)
        else:
            m += j * n
    return m

