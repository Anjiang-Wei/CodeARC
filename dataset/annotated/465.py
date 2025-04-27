def is_probable_prime(n: int) -> str:
    if n < 4:
        return 'Probable Prime'
    if n % 2 == 0:
        return 'Composite'
    
    d, r = n - 1, 0
    while d % 2 == 0:
        d, r = d // 2, r + 1
    
    for a in [2, 31]:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return 'Composite'
            if x == n - 1:
                break
        else:
            return 'Composite'
    
    return 'Probable Prime'

