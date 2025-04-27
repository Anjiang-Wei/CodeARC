def solution(N, M):
    import numpy as np
    # Create an array with numbers from 0 to N-1, reshape it into 2 sub-arrays
    arr = np.arange(N).reshape(2, -1)
    # Rotate each sub-array M times and convert to list
    result = np.roll(arr, M, axis=1).tolist()
    return result

