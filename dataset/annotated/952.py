def sum_of_integers_in_string(string: str) -> int:
    import re
    # Find all sequences of digits in the string
    numbers = re.findall(r"\d+", string)
    # Convert each found sequence to an integer and sum them up
    return sum(int(num) for num in numbers)

