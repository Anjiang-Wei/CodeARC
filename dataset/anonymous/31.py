def solution(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        solution("") => 0
        solution("abAB") => 131
        solution("abcCd") => 67
        solution("helloE") => 69
        solution("woArBld") => 131
        solution("aAaaaXa") => 153
    """

    return sum([ord(ch) for ch in s if ch.isupper()])

