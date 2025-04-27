def calculate_divisor_sum(num: int) -> int:
    res = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            res += i
            if i * i != num:
                res += num // i
        i += 1
    return res

def amicable_numbers_sum(limit: int) -> int:
    amicables = set()
    for num in range(2, limit + 1):
        if num in amicables:
            continue
        sum_fact = calculate_divisor_sum(num)
        sum_fact2 = calculate_divisor_sum(sum_fact)
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact)
    return sum(amicables)

