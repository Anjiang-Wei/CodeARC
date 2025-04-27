def are_all_narcissistic(*values: str) -> bool:
    def get_digits(n: int) -> list[int]:
        return [int(x) for x in list(str(n))]

    def is_narc(n: int) -> bool:
        return n == sum([x**len(get_digits(n)) for x in get_digits(n)])

    try:
        return all(type(n) in [int, str] and is_narc(int(n)) for n in values)
    except ValueError:
        return False

