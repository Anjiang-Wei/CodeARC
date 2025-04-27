def solution(n):
    def thirt(n):
        array = [1, 10, 9, 12, 3, 4]
        total = sum(int(c) * array[i % 6] for i, c in enumerate(reversed(str(n))))
        if n == total:
            return total
        return thirt(total)
    
    return thirt(n)

