def solution(string):
    # Check if the string can be constructed by repeating a subpattern
    return (string * 2).find(string, 1) != len(string)

