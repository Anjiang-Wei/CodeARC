def find_first_odd(nums: list[int]) -> int | None:
    first_odd = next((el for el in nums if el % 2 != 0), None)
    return first_odd

