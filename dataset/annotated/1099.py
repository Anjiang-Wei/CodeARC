def is_valid_expansion(number_list: list[int]) -> bool:
    def expand(val: int, nums: set[int], x: int, y: int, z: int) -> set[int]:
        dirs = {z}
        for num in nums.copy():
            if abs(val - num) not in (1, 5) or {val % 5, num % 5} == {0, 1}:
                continue

            nums.discard(num)
            diff = val - num
            sign = diff // abs(diff)
            nx, ny, nz = (x, z * sign, -y * sign) if abs(diff) == 1 else (-z * sign, y, x * sign)
            dirs |= expand(num, nums, nx, ny, nz)
        return dirs

    return expand(number_list.pop(), set(number_list), 1, 2, 3) == {1, 2, 3, -1, -2, -3}

