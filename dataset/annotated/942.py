def group_by_tens(*args: int) -> list:
    from collections import defaultdict
    
    if not args:
        return []
    
    tens = defaultdict(list)
    
    # Sort the numbers and group them by their tens place
    for n in sorted(args):
        tens[n // 10].append(n)
    
    # Create the result list with groups in order, using None for empty groups
    return [tens.get(d, None) for d in range(max(tens) + 1)]

