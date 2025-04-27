def is_armstrong_number(n: int) -> bool:
    num = str(n)
    length = len(num)
    # Calculate the sum of each digit raised to the power of the number of digits
    return sum(int(a) ** length for a in num) == n

