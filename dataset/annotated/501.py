def calculate_trump_score(ts: str) -> float:
    import re
    # Find all groups of repeated vowels
    x = re.findall(r'([aeiou])(\1*)', ts, re.I)
    # Calculate the number of extra vowels in each group
    y = [len(i[1]) for i in x]
    # Return the rounded Trump score
    return round(sum(y) / len(y), 2)

