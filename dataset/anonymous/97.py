def solution(nums):
    if all(x == 0 for x in nums):
        return float('inf')
    return sum(x == 0 for x in nums) / sum(x != 0 for x in nums)

