def solution(nums):
    return all(n % 2 == 1 for n in nums[1::2])

