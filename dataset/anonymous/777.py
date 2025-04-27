def solution(s):
    # Count the number of "10" patterns in the string
    # Each "10" pattern requires two flips
    # If the last character is '1', it requires an additional flip
    return s.count("10") * 2 + (s[-1] == "1")

