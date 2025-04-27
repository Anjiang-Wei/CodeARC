def solution(strng, letter):
    counter = 0
    
    for chr in strng:
        if chr == letter:
            counter += 1
    
    return counter

