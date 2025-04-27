def solution(address, n):
    '''
    Input: address (int, your house number), n (int, length of road in houses) 
    Returns: int, number of the house across from your house. 
    '''
    # The sum of opposite house numbers will always be 2n + 1
    return (2 * n + 1 - address)

