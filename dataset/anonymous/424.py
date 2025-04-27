def solution(arr):
    # For each element in the array, count how many elements to the right are smaller
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(len(arr))]

