def count_digit_occurrences(start: int, finish: int) -> list[int]:
    xs = [0] * 10
    for n in range(start, finish + 1):
        for i in str(n):
            xs[int(i)] += 1
    return xs

