def count_removals_for_alternating_chars(s: str) -> int:
    from itertools import groupby
    # Calculate the number of characters to remove by subtracting the length of grouped characters from the original length
    return len(s) - len(list(groupby(s)))

