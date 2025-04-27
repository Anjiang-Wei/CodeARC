def calculate_sequence(k: int, n: int) -> int:
    a = []
    for i in range(0, n + 1):
        if i < k:
            a.append(i + 1)
        else:
            a.append(a[-1] + a[i // k])
    return a[-1]

