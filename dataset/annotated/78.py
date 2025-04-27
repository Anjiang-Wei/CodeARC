def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1)) == 0

def differ_at_one_bit_position(a: int, b: int) -> bool:
    return is_power_of_two(a ^ b)

