def count_loose_subsequences(s1: str, s2: str) -> int:
    import re
    
    # Create a regex pattern from s1 where each character is followed by '?'
    p = re.sub(r"(.)", r"\1?", s1)
    
    # Check if all characters in s2 are in s1, if not return -1
    if set(s2) - set(s1):
        return -1
    
    # Find all matches of the pattern in s2 and return the count minus 1
    return len(re.findall(p, s2)) - 1

