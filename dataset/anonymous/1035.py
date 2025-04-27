def solution(name):
    # Calculate the weight of the name by swapping case and summing ASCII values of alphabetic characters
    return sum(ord(a) for a in name.swapcase() if a.isalpha())

