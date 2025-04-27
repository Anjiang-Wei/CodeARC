def solution(n): 
    digits = [int(digit) for digit in str(n)]
    return all(digit >= digits.count(digit) for digit in digits)

