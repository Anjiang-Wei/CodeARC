def solution(x):
    for i in range(1, len(str(x)) + 1):
        # Check if the first i digits are divisible by i
        if int(str(x)[:i]) % i != 0:
            return False
    return True

