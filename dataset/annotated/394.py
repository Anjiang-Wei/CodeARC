def calculate_z_function(str_: str) -> list[int]:
    if not str_:
        return []

    def prefix2(a: str, b: str, num: int) -> int:
        for i in range(num, -1, -1):
            if b.startswith(a[:i]):
                return i

    z = []
    k = len(str_)
    for i in range(len(str_)):
        z.append(prefix2(str_[i:], str_[:k - i], k - i))
    
    return z

