def max_digit_sum_after_split(s: str) -> int:
    return max(sum(map(int, x)) for x in s.split('0'))

