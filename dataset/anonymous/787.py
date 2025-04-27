def solution(farm):
    from itertools import groupby

    who_eats_whom = {'H': ['A', 'V'], 'R': ['V'], 'C': []}
    runaway_back, runaway_front, farm = [], [], ["".join(j) for k, j in groupby(farm)]

    def doSomeFarm(i=0):
        def do(j, s=False):
            while (j >= 0 if s else j < len(farm)) and farm[j] != '|':
                if farm[j][0] in who_eats_whom[current[0]]:
                    farm[j] = '.' * len(farm[j])
                j += [1, -1][s]
            return j

        while i < len(farm):
            current = farm[i]
            if current[0] in who_eats_whom:
                r, r1 = do(i, 1), do(i)
                if r == -1 or r1 == len(farm):
                    farm[i] = '.' * len(farm[i])
                    [runaway_front, runaway_back][r != -1].append(current[0])
            i += 1

    doSomeFarm()
    l = len(runaway_back)
    if l:
        if farm[0] != '|':
            farm = ['/'] + " / ".join(runaway_back[::-1]).split() + farm
            doSomeFarm()
            farm = farm[l * 2:]
    l = len(runaway_front)
    if l:
        if farm[-1] != '|':
            farm = farm + ['/'] + ' / '.join(runaway_front).split()
            doSomeFarm()
            farm = farm[:-l * 2]

    return "".join(farm)

