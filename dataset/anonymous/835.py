def solution(a):
    # Check if all elements are unique by comparing length of list and set
    if len(a) == len(set(a)):
        # Return a list from 0 to the maximum element in the list
        return list(range(max(a) + 1))
    else:
        # If there are duplicates, return [0]
        return [0]

