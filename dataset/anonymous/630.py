def solution(l, d, x):
    def digit_sum(num):
        # Calculate the sum of digits of the number
        return sum(map(int, str(num)))
    
    # Find all numbers in the range [l, d] with digit sum equal to x
    listOfCorrect = [num for num in range(l, d + 1) if digit_sum(num) == x]
    
    # Return the minimum and maximum of the found numbers
    return [min(listOfCorrect), max(listOfCorrect)]

