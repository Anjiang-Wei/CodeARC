def interpret_language(s: str) -> str:
    from operator import add, mul, floordiv as fdiv, pow

    def updateMem(func, v):
        mem[p] = func(mem.get(p, 0), v) % 256

    braces, stack = {}, []
    for i, c in enumerate(s):
        if c == 'W':
            stack.append(i)
        if c == 'E':
            braces[i] = stack[-1]
            braces[stack.pop()] = i

    mem, copy, output = {}, 0, []
    p, i = 0, 0
    while i < len(s):
        cmd = s[i]
        if cmd == '>':
            p += 1
        elif cmd == '<':
            p -= 1
        elif cmd == 'p':
            mem[p] = copy
        elif cmd == 'c':
            copy = mem.get(p, 0)
        elif cmd == 'W':
            i = i if bool(mem.get(p, 0)) else braces[i]
        elif cmd == 'E':
            i = braces[i] if mem.get(p, 0) else i
        elif cmd == 'P':
            output.append(chr(mem.get(p, 0)))
        elif cmd == 'N':
            output.append(str(mem.get(p, 0)))
        elif cmd == '+':
            updateMem(add, 1)
        elif cmd == '-':
            updateMem(add, -1)
        elif cmd == 'L':
            updateMem(add, 2)
        elif cmd == 'I':
            updateMem(add, -2)
        elif cmd == 'T':
            updateMem(mul, 2)
        elif cmd == 'V':
            updateMem(fdiv, 2)
        elif cmd == 'Q':
            updateMem(pow, 2)
        elif cmd == 'U':
            updateMem(lambda a, b: int(pow(a, b)), .5)
        elif cmd == 'A':
            updateMem(add, copy)
        elif cmd == 'B':
            updateMem(add, -copy)
        elif cmd == 'Y':
            updateMem(mul, copy)
        elif cmd == 'D':
            updateMem(fdiv, copy)
        i += 1

    return ''.join(output)

