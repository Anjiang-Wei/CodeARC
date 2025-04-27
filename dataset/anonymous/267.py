def solution(a, b):
    # Calculate the sum of squares of elements in array a
    sum_of_squares = sum(x ** 2 for x in a)
    
    # Calculate the sum of cubes of elements in array b
    sum_of_cubes = sum(x ** 3 for x in b)
    
    # Return True if sum of squares is greater than sum of cubes
    return sum_of_squares > sum_of_cubes

