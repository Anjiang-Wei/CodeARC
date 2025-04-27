def solution(comb1, comb2):
    def mesh(a, b):
        for i in range(len(a)):
            for j, k in zip(a[i:], b):
                if j + k == '**': 
                    break
            else:
                return max(i + len(b), len(a))
        return len(a) + len(b)
    
    return min(mesh(comb1, comb2), mesh(comb2, comb1))

