def power_at_index(array: list, n: int) -> int:
    try:
        return array[n] ** n
    except IndexError:
        return -1

