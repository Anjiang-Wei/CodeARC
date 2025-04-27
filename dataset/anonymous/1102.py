def solution(lst):
    ret = []
    while lst:
        ret.append(lst[-1])
        # Calculate the differences between consecutive elements
        lst = [a - b for a, b in zip(lst, lst[1:])]
    # Reverse the result to get the original list
    return ret[::-1]

