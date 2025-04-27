def solution(p):
    new_p = [(0, 0)]
    new_str = ''
    x, y = 0, 0

    for i in p:
        if i == '<':
            x -= 1
        elif i == '>':
            x += 1
        elif i == '^':
            y += 1
        elif i == 'v':
            y -= 1

        if (x, y) not in new_p:
            new_p.append((x, y))
            new_str += i
        else:
            for j in new_p[::-1]:
                if j != (x, y):
                    new_p.pop()
                    new_str = new_str[:-1]
                else:
                    break

    return new_str

