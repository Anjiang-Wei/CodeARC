def rearrange_sevens_eights_nines(arr: list[int]) -> list[int]:
    import re
    
    ss, s = '', ''.join(map(str, arr))
    while ss != s:
        ss, s = s, re.sub(r'(7+)(89)', r'\2\1', s)
    
    return list(map(int, s))

