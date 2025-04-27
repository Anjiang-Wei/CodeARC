def solution(arr, newavg):
    from math import ceil
    
    # Calculate the required donation to reach the desired average
    value = int(ceil((len(arr) + 1) * newavg - sum(arr)))
    
    # If the calculated donation is non-positive, raise an error
    if value < 0:
        raise ValueError
    
    return value

