def solution(n):
    result = []
    
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        result.append(product)
        n = product
    
    return result

