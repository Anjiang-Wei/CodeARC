def solution(s):
    def insert_missing_letters(s):
        lst, found, inside = [], set(), set(s.upper())
        for a in s:
            if a in found:
                lst.append(a)
            else:
                lst.append(a + ''.join(c for c in map(chr, range(ord(a) - 31, 91)) if c not in inside))
            found.add(a)
        return ''.join(lst)
    
    return insert_missing_letters(s)

