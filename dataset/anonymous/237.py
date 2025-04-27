def solution(s):
    from re import findall
    # Use regex to find all big groups in the string
    return len(findall(r"((.)\2+(?!\2)){2,}", s))

