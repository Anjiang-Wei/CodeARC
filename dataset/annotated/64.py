def product_of_odd_digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    product_of_odd_digits(1)  == 1
    product_of_odd_digits(4)  == 0
    product_of_odd_digits(235) == 15
    """
    has_odd, prod = False, 1
    for ch in str(n):
        if int(ch) % 2 == 1:
            has_odd = True
            prod *= int(ch)
    return 0 if not has_odd else prod

