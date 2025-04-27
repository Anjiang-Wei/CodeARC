def reduce_to_sevens(m: int) -> tuple[int, int]:
    def seven(m: int, step: int = 0) -> tuple[int, int]:
        if m < 100:
            return (m, step)
        x, y = divmod(m, 10)
        res = x - 2 * y
        return seven(res, step + 1)
    
    return seven(m)

