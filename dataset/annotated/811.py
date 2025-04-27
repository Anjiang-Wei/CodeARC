def find_longest_adjacent_punctuation(stg: str) -> str:
    import re
    
    matches = re.findall(r"(!+|\?+)", stg)
    # Generate combinations of adjacent matches and find the longest one
    return max((f"{a}{b}" for a, b in zip(matches, matches[1:])), key=len, default="")

