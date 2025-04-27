def solution(s, mode='encode'):
    """
    :type s: str
    :type mode: str ('encode' or 'decode')
    :rtype: str
    """
    # Define the substitution dictionary
    substitution_dict = {i[0]: i[1] for i in [
        'GA', 'DE', 'RY', 'PO', 'LU', 'KI', 
        'AG', 'ED', 'YR', 'OP', 'UL', 'IK',
        'ga', 'de', 'ry', 'po', 'lu', 'ki', 
        'ag', 'ed', 'yr', 'op', 'ul', 'ik'
    ]}
    
    # Invert the dictionary if mode is 'decode'
    if mode == 'decode':
        substitution_dict = {v: k for k, v in substitution_dict.items()}
    
    # Function to perform substitution
    def substitute(text):
        return ''.join([substitution_dict[char] if char in substitution_dict else char for char in text])
    
    # Return the result based on the mode
    return substitute(s)

