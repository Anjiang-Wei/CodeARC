def reverse_central_slice(lst: list) -> list:
    l = len(lst) // 2 - 1
    return lst[l:-l][::-1] if l >= 0 else lst[::-1]

