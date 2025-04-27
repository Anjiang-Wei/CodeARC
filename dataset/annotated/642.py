def count_bin_occurrences(lst: list[int], binWidth: int) -> list[int]:
    # Convert each number to its corresponding bin index
    lst = [n // binWidth for n in lst]
    # Find the number of bins needed
    m = max(lst, default=-1) + 1
    # Count occurrences of each bin index
    return [lst.count(n) for n in range(m)]

