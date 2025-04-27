def solution(arr):
    def oddity(n):
        while True:
            n, m = divmod(n, 2)
            yield m

    res = arr[0]
    for n in arr[1:]:
        if next(b > a for a, b in zip(oddity(res), oddity(n)) if a != b):
            res = n
    return res

