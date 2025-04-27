def find_two_sum_indices(nums: list[int], target: int) -> tuple[int, int]:
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == target:
                return (i, j)

