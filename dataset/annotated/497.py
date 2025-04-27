def sort_numbers_by_digit_sum(number_string: str) -> str:
    def digit_sum(x: str) -> int:
        # Calculate the sum of digits of the number
        return sum(int(c) for c in x)
    
    # Split the string into numbers, sort by digit sum, then by string value
    return ' '.join(sorted(sorted(number_string.split()), key=digit_sum))

