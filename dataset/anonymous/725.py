def solution(arr):
    from itertools import count
    
    def pair_zeros(arr):
        c = count(1)
        # Iterate through the array, keeping zeros only if they are the first in a pair
        return [elem for elem in arr if elem != 0 or next(c) % 2]
    
    return pair_zeros(arr)

