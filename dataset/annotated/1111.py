from typing import List

def generate_tribonacci_sequence(signature: List[float], n: int) -> List[float]:
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res

