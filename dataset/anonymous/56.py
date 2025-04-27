def solution(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if all(x >= 0 for x in nums): return min(nums)
    s, ans = 0, float('inf')
    for x in nums:
        s += x
        ans = min(ans, s)
        if s >= 0: s = 0
    return ans

