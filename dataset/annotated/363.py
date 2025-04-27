def convert_to_ternary_representation(n: int) -> str:
    import numpy as np
    
    s = np.base_repr(n, 3)
    if '2' in s:
        return 'Impossible'
    
    # Create the result string by identifying positions of '1' in the base-3 representation
    result = '+'.join(['3^{}'.format(i) for i, d in enumerate(s[::-1]) if d == '1'][::-1])
    
    return result

