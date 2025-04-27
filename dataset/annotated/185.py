def find_self_divisible_numbers(startnum: int, endnum: int) -> list[int]:
    return [n for n in range(startnum, endnum + 1) 
            if not any(map(lambda x: int(x) == 0 or n % int(x) != 0, str(n)))]

