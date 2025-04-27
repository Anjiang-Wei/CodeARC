def count_smaller_elements_to_right(arr: list[int]) -> list[int]:
    # For each element in the array, count how many elements to the right are smaller
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(len(arr))]

