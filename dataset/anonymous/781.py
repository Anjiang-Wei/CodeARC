def solution(value):
    # Calculate the sum of each digit raised to the power of the number of digits
    return value == sum(int(x) ** len(str(value)) for x in str(value))

