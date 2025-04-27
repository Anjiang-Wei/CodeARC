def longest_valid_parentheses(s: str) -> int:
    res, pos = 0, [0]
    for i, b in enumerate(s, 1):
        if b == "(":
            pos.append(i)
        else:
            try:
                pos.pop()
                res = max(res, i - pos[-1])
            except IndexError:
                pos.append(i)
    return res

