def sum_of_indices_for_pair(arr: list[int], n: int) -> int:
    s = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if j in s or i in s:
                continue
            if arr[i] + arr[j] == n:
                s.append(i)
                s.append(j)
    return sum(s)

