def div_sum(num):
    res = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            res += i
            if i * i != num:
                res += num // i
        i += 1
    return res

def solution(limit):
    amicables = set()
    for num in range(2, limit + 1):
        if num in amicables:
            continue
        sum_fact = div_sum(num)
        sum_fact2 = div_sum(sum_fact)
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact)
    return sum(amicables)

