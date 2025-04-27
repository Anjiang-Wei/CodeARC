def is_single_digit_sum_even(n: int) -> bool:
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return n % 2 == 0

