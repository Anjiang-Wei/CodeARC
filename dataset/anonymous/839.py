def solution(digits, n):
    if n > len(digits):
        raise ValueError("n is larger than the length of the string")
    # Generate slices of length n
    return [[int(digit) for digit in digits[i:i+n]] for i in range(len(digits) - n + 1)]

