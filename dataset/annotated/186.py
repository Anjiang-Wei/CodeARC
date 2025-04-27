def is_min_heap_recursive(arr: list, i: int) -> bool:
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and is_min_heap_recursive(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or \
                  (arr[i] <= arr[2 * i + 2] and \
                   is_min_heap_recursive(arr, 2 * i + 2))
    return left_child and right_child

def is_min_heap(arr: list) -> bool:
    return is_min_heap_recursive(arr, 0)

