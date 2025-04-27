def solution(string1, string2):
    return len(set(string1)) == len(set(string2)) == len(set(zip(string1, string2)))

