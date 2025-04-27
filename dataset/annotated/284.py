def classify_number_by_ones_count(n: int) -> str:
    # Count the number of 1's in the binary representation of n
    # If the count is even, it's Evil; if odd, it's Odious
    return "It's %s!" % ["Evil", "Odious"][bin(n).count("1") % 2]

