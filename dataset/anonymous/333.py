def solution(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    # Create a new list where even numbers remain in place and odd numbers are sorted
    return [x if x % 2 == 0 else odds.pop() for x in arr]

