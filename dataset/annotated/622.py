def find_nth_digit_from_end(num: int, nth: int) -> int:
    if nth <= 0:
        return -1
    try:
        # Convert number to string, remove negative sign, and get the nth digit from the end
        return int(str(num).lstrip('-')[-nth])
    except IndexError:
        # If nth is larger than the number of digits, return 0
        return 0

