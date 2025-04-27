def solution(section1, section2):
    def version(s):
        v = [int(n) for n in s.split(".")]
        while v[-1] == 0:
            v = v[:-1]
        return v

    v1, v2 = version(section1), version(section2)
    return -1 if v1 < v2 else 1 if v1 > v2 else 0

