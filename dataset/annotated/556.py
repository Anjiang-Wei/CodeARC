def max_number_by_removing_one_digit(n: int) -> int:
    s = str(n)
    # Generate all possible numbers by removing one digit at a time
    return int(max(s[:i] + s[i+1:] for i in range(len(s))))

