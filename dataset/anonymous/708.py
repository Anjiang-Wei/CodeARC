def solution(string):
    DIGITS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Calculate the base 10 value by iterating over the reversed string
    return sum(DIGITS.index(digit) * 64**i for i, digit in enumerate(string[::-1]))

