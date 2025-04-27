def check_even_position_parity(nums: list[int]) -> bool:
    return all(nums[i] % 2 == i % 2 for i in range(len(nums)))

