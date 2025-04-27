def solution(n):
    from bisect import bisect_left

    def generate_palindromic_squares(limit):
        l, p = [1], []
        for num in range(2, int(limit ** 0.5) + 1):
            l = [num * num + j for j in [0] + l]
            p += [int(k) for k in map(str, l[1:]) if k == k[::-1]]
        return sorted(set(p))

    palindromic_squares = generate_palindromic_squares(10 ** 7)
    return bisect_left(palindromic_squares, n)

