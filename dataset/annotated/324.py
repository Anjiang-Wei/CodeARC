def product_except_self(nums: list[int]) -> list[int]:
    from functools import reduce
    
    z = nums.count(0)
    if z > 1:
        return [0] * len(nums)
    
    p = reduce(int.__mul__, (v for v in nums if v))
    
    # If there is one zero, return p for zero positions, else return p divided by each element
    return [not v and p for v in nums] if z else [p // v for v in nums]

