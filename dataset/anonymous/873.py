def solution(arr):
    if len(arr) < 3:
        return 0
    
    res, value, save = 0, arr[1] - arr[0], arr[:2]
    
    for x, y in zip(arr[1:], arr[2:]):
        if y - x == value:
            save.append(y)
        else:
            if len(save) >= 3:
                res += sum(save)
            value, save = y - x, [x, y]
    
    if len(save) >= 3:
        res += sum(save)
    
    return res

