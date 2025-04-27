def solution(n, d):
    cnt = 0
    for a in range(12, n + 1):
        nums = list(map(int, str(a)))
        # Check if digits are in increasing order and unique
        if nums == sorted(set(nums)) and \
                all(c - b <= d for b, c in zip(nums[:-1], nums[1:])):
            cnt += 1
    return cnt

