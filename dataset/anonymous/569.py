def solution(arr1, arr2):
    if not arr1 and not arr2:
        return []
    elif not arr1 or not arr2:
        return arr1 or arr2
    else:
        # Convert each array to a string, then to an integer, and sum them
        s = int(''.join(map(str, arr1))) + int(''.join(map(str, arr2)))
        # Check if the result is negative
        minus = s < 0
        # Convert the sum back to a list of digits
        return [int(x) * -1 if minus and i == 0 else int(x) for i, x in enumerate(str(abs(s)))]

