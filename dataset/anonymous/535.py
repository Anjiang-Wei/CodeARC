def solution(numbers):
    # Create a list comprehension to filter numbers with even counts
    return [i for i in numbers if numbers.count(i) % 2 == 0]

