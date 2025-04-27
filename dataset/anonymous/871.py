def solution(nums, target):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == target:
                return (i, j)

