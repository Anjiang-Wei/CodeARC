def difference_product_sum_of_digits(n: int) -> int:
    stringInt = str(n)
    product = 1
    sum_digits = 0
    for i in stringInt:
        product *= int(i)
        sum_digits += int(i)
    return product - sum_digits

