def solution(nums):
    return all(nums[i] % 2 == i % 2 for i in range(len(nums)))

