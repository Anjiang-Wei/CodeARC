def solution(*arr):
    if not arr: 
        return ''
    # Find the length of the largest number to determine the width
    ln = len(str(max(arr)))
    # Format each number with leading zeros and join them with newline characters
    return '\n'.join(str(c).zfill(ln) for c in arr)

