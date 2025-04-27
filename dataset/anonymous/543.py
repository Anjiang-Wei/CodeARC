def solution(arr):
    def key(x):
        # Translate 3 to 7 and 7 to 3, then convert back to integer for sorting
        return int(str(x).translate(str.maketrans('37', '73')))
    
    # Sort the array using the custom key
    return sorted(arr, key=key)

