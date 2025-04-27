def min_coins_for_change(coins_list: list[int], amount_of_change: int) -> int:
    from collections import deque
    
    q = deque([(0, amount_of_change)])
    
    while q:
        l, a = q.popleft()
        if a == 0:
            return l
        q.extend((l + 1, a - i) for i in coins_list if a >= i)

