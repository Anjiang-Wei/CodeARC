def solution(L, R):
    def digit_sum(x):
        return sum(map(int, str(x)))

    def is_comfortable(a, b):
        return a != b and b in range(a - digit_sum(a), a + digit_sum(a) + 1)

    count = 0
    for a in range(L, R + 1):
        for b in range(a + 1, R + 1):
            if is_comfortable(a, b) and is_comfortable(b, a):
                count += 1

    return count

