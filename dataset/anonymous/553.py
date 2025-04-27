def solution(arr):
    # Check if all elements are integers
    if all(type(n) == int for n in arr):
        # Calculate the sum of cubes of odd numbers
        return sum(n**3 for n in arr if n % 2)
    else:
        # Return None if any element is not an integer
        return None

