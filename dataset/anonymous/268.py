def solution(arr):
    def can_jump(arr):
        if arr[0] == 0 or len(arr) == 1:
            return False
        
        if arr[0] >= len(arr):
            return True
        
        for jump in range(1, arr[0] + 1):
            if can_jump(arr[jump:]):
                return True
        
        return False
    
    return can_jump(arr)

