def calculate_expression(n: str) -> float:
    def evaluate(s: list, r: float = 0, o: int = 0, x: str = '', c: str = '') -> float:
        while s and ')' != c:
            c = s.pop(0)
            i = '+-*/)('.find(c)
            if c == '-' > x or i < 0:
                x += c
            elif c == '(':
                x = str(evaluate(s))
            elif i > -1:
                a = float(x)
                r = [r + a, r - a, r * a, r / a][o]
                o = i
                x = ''
        return r

    return evaluate([*n, '+'])

