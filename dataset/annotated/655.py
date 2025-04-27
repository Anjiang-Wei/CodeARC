def compare_even_odd(arr: list[int]) -> bool:
    maxEven, minOdd = (
        f(
            filter(lambda n: n % 2 == v, arr),
            default=float("-inf") if v == 0 else float("inf"),
        )
        for f, v in ((max, 0), (min, 1))
    )
    return maxEven < minOdd

