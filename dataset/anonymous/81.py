def solution(string, second_string): 
    for char in second_string:
        string = string.replace(char, '')
    return string

