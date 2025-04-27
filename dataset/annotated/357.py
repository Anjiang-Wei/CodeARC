def are_isomorphic_strings(s1: str, s2: str) -> bool:
    return len(set(zip(s1, s2))) == len(set(s1)) == len(set(s2))

