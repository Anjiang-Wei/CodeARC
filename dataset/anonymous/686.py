def solution(fmt, nbr, start):
    # Check for edge cases
    if not isinstance(start, int) or nbr <= 0 or not isinstance(nbr, int):
        return []
    
    # Check if the format contains the placeholder
    if '<index_no>' not in fmt:
        return [fmt] * nbr
    
    # Generate the formatted file names
    return [fmt.replace('<index_no>', '{0}').format(i) for i in range(start, start + nbr)]

