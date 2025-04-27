def calculate_stirling_number(n: int, k: int) -> int:
    from math import factorial as fact

    if k < 0 or k > n:
        return 'It cannot be possible!'
    
    # Calculate Stirling numbers of the second kind
    result = sum(
        [1, -1][i % 2] * (k - i) ** n * fact(k) // (fact(k - i) * fact(i))
        for i in range(k + 1)
    ) // fact(k)
    
    return result

