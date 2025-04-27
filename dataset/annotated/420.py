def find_digit_power_matches(a: int, b: int) -> list:
    def dig_pow(n: int) -> int:
        # Calculate the sum of digits raised to their respective positions
        return sum(int(x) ** y for y, x in enumerate(str(n), 1))
    
    # Collect numbers that satisfy the property in the given range
    return [x for x in range(a, b + 1) if x == dig_pow(x)]

