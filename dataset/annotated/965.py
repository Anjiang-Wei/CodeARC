def closest_to_zero(numbers: str) -> int:
    if len(numbers) == 0:
        return 0
    
    x = numbers.split(" ")
    poz = []
    neg = []
    
    for i in x:
        num = int(i)
        if num == 0:
            return 0
        if num > 0:
            poz.append(num)
        if num < 0:
            neg.append(num)
    
    # If both lists are empty, return 0
    if not poz and not neg:
        return 0
    
    # Determine the closest to zero
    min_poz = min(poz) if poz else float('inf')
    max_neg = max(neg) if neg else float('-inf')
    
    if 0 - min_poz == max_neg:
        return min_poz
    if 0 - min_poz > max_neg:
        return min_poz
    else:
        return max_neg

