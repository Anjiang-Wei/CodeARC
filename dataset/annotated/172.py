def calculate_pairwise_xor_sum(arr: list[int], n: int) -> int:
    ans = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            ans = ans + (arr[i] ^ arr[j])
    return ans

