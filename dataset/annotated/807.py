def translate_with_caesar_cipher(st: str) -> str:
    from string import ascii_lowercase as al
    tbl = str.maketrans(al, al[10:] + al[:10])
    return st.translate(tbl)

