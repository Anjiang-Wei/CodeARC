def solution(num1, num2):
    return any(i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789')

