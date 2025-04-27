def solution(s):
    # Calculate the sum of alphabetical positions for each character in the string
    return sum(ord(c) - 96 for c in s)

