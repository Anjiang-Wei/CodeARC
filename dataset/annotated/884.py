def convert_to_single_digit(n: int) -> int:
    for _ in range(150):
        # Determine the base by finding the maximum digit and adding 1
        # If '9' is present, add an additional 1 to the base
        base = int(max(str(n))) + 1 + ('9' in str(n))
        # Convert the number to base 10 from the determined base
        n = int(str(n), base)
        # If the number is reduced to a single digit, return it
        if n < 10:
            return n
    # If not reduced to a single digit after 150 iterations, return -1
    return -1

