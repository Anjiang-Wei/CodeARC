def calculate_zero_to_nonzero_ratio(nums: list[int]) -> float:
    if all(x == 0 for x in nums):
        return float('inf')
    return sum(x == 0 for x in nums) / sum(x != 0 for x in nums)

