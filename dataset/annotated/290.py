def calculate_extra_candies_needed(s: list[int]) -> int:
    if not s or len(s) == 1:
        return -1
    # Calculate the total candies needed to make all equal to the max
    return len(s) * max(s) - sum(s)

