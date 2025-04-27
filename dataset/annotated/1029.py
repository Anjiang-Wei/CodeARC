def find_pandigital_numbers(val: int, n: int, k: int) -> list:
    def is_pandigital(num: int) -> bool:
        s = str(num)
        return '0' not in s and len(set(s)) == len(s)

    if n <= 0 or k <= 0:
        return []
    
    result = []
    current = val
    
    while len(result) < k:
        if current > 0 and is_pandigital(current) and len(str(current)) == n:
            result.append(current)
        current += 1
    
    return result

