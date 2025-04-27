from typing import List

def find_unique_string(a: List[str]) -> str:
    from collections import defaultdict
    
    d = {}
    c = defaultdict(int)
    
    for e in a:
        # Create a frozenset of the characters in the string, ignoring spaces and case
        t = frozenset(e.strip().lower())
        # Map the frozenset to the original string
        d[t] = e
        # Count occurrences of each frozenset
        c[t] += 1
    
    # Find the frozenset that occurs only once and return the corresponding original string
    return d[next(filter(lambda k: c[k] == 1, c))]

