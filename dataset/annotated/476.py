def consecutive_count_compress(s: str, n: int) -> str:
    from re import sub
    
    for _ in range(1, n):
        s = sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    
    return s

