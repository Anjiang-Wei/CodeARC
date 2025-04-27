def insert_and_complete_missing_letters(s: str) -> str:
    lst, found, inside = [], set(), set(s.upper())
    for a in s:
        if a in found:
            lst.append(a)
        else:
            lst.append(a + ''.join(c for c in map(chr, range(ord(a) - 31, 91)) if c not in inside))
        found.add(a)
    return ''.join(lst)

def insert_and_complete(s: str) -> str:
    return insert_and_complete_missing_letters(s)

