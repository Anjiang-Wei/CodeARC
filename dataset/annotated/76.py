def count_even_odd_digits(num: int) -> tuple[int, int]:
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

     Example:
        count_even_odd_digits(-12) ==> (1, 1)
        count_even_odd_digits(123) ==> (1, 2)
    """

    even, odd = 0, 0
    for ch in str(abs(num)):
        if ch in "02468": even += 1
        if ch in "13579": odd += 1
    return even, odd

