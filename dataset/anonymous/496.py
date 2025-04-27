def solution(m):
    def seven(m, step=0):
        if m < 100:
            return (m, step)
        x, y = divmod(m, 10)
        res = x - 2 * y
        return seven(res, step + 1)
    
    return seven(m)

