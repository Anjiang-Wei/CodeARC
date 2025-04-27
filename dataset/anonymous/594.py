def solution(num):
    num = str(num)
    count = 0
    while len(num) > 1:
        product = 1
        for digit in num:
            product *= int(digit)
        num = str(product)
        count += 1
    return count

