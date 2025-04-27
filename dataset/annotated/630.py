def find_min_max_with_digit_sum(l: int, d: int, x: int) -> list[int]:
    def digit_sum(num: int) -> int:
        # Calculate the sum of digits of the number
        return sum(map(int, str(num)))
    
    # Find all numbers in the range [l, d] with digit sum equal to x
    listOfCorrect = [num for num in range(l, d + 1) if digit_sum(num) == x]
    
    # Return the minimum and maximum of the found numbers
    return [min(listOfCorrect), max(listOfCorrect)]

