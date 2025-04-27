def solution(num):
    if type(num) is not int or num < 0:
        return "Not valid"
    return num == int(str(num)[::-1])

