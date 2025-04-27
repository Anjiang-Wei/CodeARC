def find_largest_oddity_number(arr: list[int]) -> int:
    def oddity(n: int):
        while True:
            n, m = divmod(n, 2)
            yield m

    res = arr[0]
    for n in arr[1:]:
        if next(b > a for a, b in zip(oddity(res), oddity(n)) if a != b):
            res = n
    return res

