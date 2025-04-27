def format_and_sort_array(arr: list[int]) -> str:
    def extract(arr: list[str]) -> str:
        return ''.join(arr[:2] + arr[-2:])

    arr = list(map(chr, arr))
    w1 = extract(arr)
    arr.sort()
    w2 = extract(arr)
    
    return f'{w1}-{w2}-{w2[::-1]}-{w2}'

