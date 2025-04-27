def is_digit_count_valid(number: int) -> bool: 
    digits = [int(digit) for digit in str(number)]
    return all(digit >= digits.count(digit) for digit in digits)

