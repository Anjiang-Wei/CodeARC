def expanded_form(n: int) -> str:
    output = []
    exp = 0
    
    while n:
        n, r = divmod(n, 10)
        if r:
            output.append(f"{r}*{10**exp}" if exp else f"{r}")
        exp += 1
    
    return "+".join(output[::-1])

