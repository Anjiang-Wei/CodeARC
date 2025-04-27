def solution(st):
    from string import ascii_lowercase as al
    tbl = str.maketrans(al, al[10:] + al[:10])
    return st.translate(tbl)

