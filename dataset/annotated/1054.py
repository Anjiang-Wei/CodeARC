def find_single_digit_average(input: int) -> int:
    digits = [int(c) for c in str(input)]
    while len(digits) > 1:
        # Calculate the average of each pair of consecutive digits, rounding up
        digits = [(a + b + 1) // 2 for a, b in zip(digits, digits[1:])]
    return digits[0]

