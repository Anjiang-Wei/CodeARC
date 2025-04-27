def solution(nums, k):
    from collections import defaultdict

    count = 0
    if k < 0:
        return count
    if k == 0:
        new_nums = defaultdict(int)
        for i in nums:
            new_nums[i] += 1
        for value in new_nums:
            if new_nums[value] > 1:
                count += 1
        return count
    if k > 0:
        nums = set(nums)
        for i in nums:
            if i + k in nums:
                count += 1
        return count

