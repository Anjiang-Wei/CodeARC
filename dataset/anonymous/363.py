def solution(n):
    import numpy as np
    
    s = np.base_repr(n, 3)
    if '2' in s:
        return 'Impossible'
    
    # Create the result string by identifying positions of '1' in the base-3 representation
    result = '+'.join(['3^{}'.format(i) for i, d in enumerate(s[::-1]) if d == '1'][::-1])
    
    return result

