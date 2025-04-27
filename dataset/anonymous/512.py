def solution(array):
    inv_count = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                inv_count += 1
    return inv_count

