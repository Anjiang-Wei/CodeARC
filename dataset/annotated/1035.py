def calculate_name_weight(name: str) -> int:
    # Calculate the weight of the name by swapping case and summing ASCII values of alphabetic characters
    return sum(ord(a) for a in name.swapcase() if a.isalpha())

