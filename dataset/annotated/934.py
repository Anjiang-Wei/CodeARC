def find_max_number_in_string(s: str) -> int:
    import re
    # Find all number groupings in the string and convert them to integers
    numbers = map(int, re.findall(r"(\d+)", s))
    # Return the maximum number found
    return max(numbers)

