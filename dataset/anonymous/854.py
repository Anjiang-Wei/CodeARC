def solution(string, array):
    # Sort the characters of the string based on the order specified by the array
    return "".join(v for _, v in sorted(zip(array, string)))

