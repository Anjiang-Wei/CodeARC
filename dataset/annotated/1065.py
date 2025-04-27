def count_balloon_instances(text: str) -> int:
    from collections import defaultdict
    
    memo = defaultdict(int)
    for t in text:
        if t in 'balon':
            memo[t] += 1
    
    # 'b', 'a', 'n' are needed once, 'l', 'o' are needed twice
    count_once = min(memo['b'], memo['a'], memo['n'])
    count_twice = min(memo['l'], memo['o'])
    
    # The number of "balloon" instances is limited by the least available required character
    return min(count_once, count_twice // 2)

