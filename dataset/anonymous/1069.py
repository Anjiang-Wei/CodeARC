def solution(nums):
    return sum(a > b for i, a in enumerate(nums) for b in nums[i + 1:])

