def process_string_with_backspaces(s: str) -> str:
    stk = []
    for c in s:
        if c == '#' and stk:
            stk.pop()
        elif c != '#':
            stk.append(c)
    return ''.join(stk)

