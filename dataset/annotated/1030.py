def format_license_key(S: str, K: int) -> str:
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    # Remove dashes and convert to uppercase
    S = S.replace('-', '').upper()[::-1]
    
    # Create groups of size K
    grouped = [S[i:i+K] for i in range(0, len(S), K)]
    
    # Join groups with dashes and reverse the result
    return '-'.join(grouped)[::-1]

