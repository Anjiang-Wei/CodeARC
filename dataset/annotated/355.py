def binary_to_signed_list(n: int) -> list[int]:
    return [(c == '1') * 2 - 1 for c in '1' + bin(n)[2:-1]]

