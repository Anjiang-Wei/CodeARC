def multiply_until_single_digit(n: int) -> list[int]:
    result = []
    
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        result.append(product)
        n = product
    
    return result

