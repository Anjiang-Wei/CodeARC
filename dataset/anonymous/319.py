def solution(kanga1, rate1, kanga2, rate2):
    if rate1 == rate2:
        return kanga1 == kanga2
    cross, remainder = divmod(kanga1 - kanga2, rate2 - rate1)
    # Check if they meet at a non-negative step and remainder is zero
    return cross >= 0 and remainder == 0

