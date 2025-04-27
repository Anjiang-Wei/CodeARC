def sum_of_numbers_in_string(s: str) -> int:
    import re
    # Find all sequences of digits in the string and convert them to integers, then sum them up
    return sum(int(x) for x in re.findall(r"(\d+)", s))

