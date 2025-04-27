def solution(sum_limit):
    for p in [7, 97, 16057, 19417, 43777, 1091257, 1615837, 1954357, 2822707, 2839927, 3243337, 3400207, 6005887]:
        # Check if the sum of the sextuplet exceeds the sum_limit
        if p * 6 + 48 > sum_limit:
            # Return the sextuplet
            return [p, p + 4, p + 6, p + 10, p + 12, p + 16]

