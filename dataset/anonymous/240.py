def solution(x, y):
    product = 0
    while y != 0:
        if y % 2 == 1:
            product += x
        x += x
        y //= 2
    return product

