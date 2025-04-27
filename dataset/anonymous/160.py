def solution(number):
    order = len(str(number))
    return sum([int(i) ** order for i in str(number)]) == number

