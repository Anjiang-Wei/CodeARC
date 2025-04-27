from typing import List

def limit_occurrences(lst: List[int], N: int) -> List[int]:
    def delete_nth(order: List[int], max_e: int) -> List[int]:
        ans = []
        for o in order:
            if ans.count(o) < max_e:
                ans.append(o)
        return ans
    
    return delete_nth(lst, N)

