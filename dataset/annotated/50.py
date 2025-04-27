def compute_rounded_binary_avg(n: int, m: int) -> int | str:
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    compute_rounded_binary_avg(1, 5) => "0b11"
    compute_rounded_binary_avg(7, 5) => -1
    compute_rounded_binary_avg(10, 20) => "0b1111"
    compute_rounded_binary_avg(20, 33) => "0b11010"
    """

    if n > m: return -1
    avg = round((n + m) / 2)
    return bin(avg)

