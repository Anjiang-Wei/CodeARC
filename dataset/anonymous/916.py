def solution(val):
    def unique_digits(n):
        return len(set(str(n))) == len(str(n))
    
    val += 1
    while val % 3: 
        val += 1
    if val % 2 == 0: 
        val += 3
    
    while not unique_digits(val):
        val += 6
        if val > 9876543210: 
            break
    else:
        return val
    
    return "There is no possible number that fulfills those requirements"

