def solution(s):
    def count_carries(pair):
        carry, carried = 0, 0
        for a, b in zip(*map(lambda ss: map(int, ss[::-1]), pair.split())):
            carried += a + b
            carry += carried > 9
            carried //= 10
        return carry

    results = []
    for ab in s.split('\n'):
        carry_count = count_carries(ab)
        if carry_count == 0:
            results.append("No carry operation")
        else:
            results.append(f"{carry_count} carry operations")
    
    return '\n'.join(results)

