def solution(s):
    m, n = '', 1
    for j in s:
        if j.isdigit():
            n = int(j)
        else:
            m += j * n
    return m

