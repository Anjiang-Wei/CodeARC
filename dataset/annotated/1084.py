def count_baby_words(x: str) -> int | str:
    x = x.lower()
    # Count the occurrences of 'a', 'b', and 'y'
    # 'b' needs to be counted twice since 'baby' has two 'b's
    count_a = x.count('a')
    count_b = x.count('b') // 2
    count_y = x.count('y')
    
    # Calculate the minimum count to determine the number of 'baby' words
    baby_count = min(count_a, count_b, count_y)
    
    # If no 'baby' is found, return the specified message
    return baby_count or "Where's the baby?!"

