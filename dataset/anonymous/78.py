def solution(x: int): 
    return x > 0 and (x & (x - 1)) == 0

def differ_At_One_Bit_Pos(a: int, b: int):
    return solution(a ^ b)

