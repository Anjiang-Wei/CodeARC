def compare_versions(section1: str, section2: str) -> int:
    def version(s: str) -> list[int]:
        v = [int(n) for n in s.split(".")]
        while v[-1] == 0:
            v = v[:-1]
        return v

    v1, v2 = version(section1), version(section2)
    return -1 if v1 < v2 else 1 if v1 > v2 else 0

