def solution(lst, N):
    def delete_nth(order, max_e):
        ans = []
        for o in order:
            if ans.count(o) < max_e:
                ans.append(o)
        return ans
    
    return delete_nth(lst, N)

