def solution(arr):
    result = 0  # final result
    partial = 0 # partial sum
    # stimulate the recursion
    while arr != []:
        partial = arr[-1] * (1 + partial)
        result += partial
        arr.pop()
    return result

