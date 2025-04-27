def organize_string_with_dashes(s: str) -> str:
    from collections import Counter
    
    def sort_key(c: str) -> tuple:
        # Sort by digit, then uppercase, then character itself
        return (c.isdigit(), c.isupper(), c)
    
    answer = []
    counter = Counter(s)
    
    while counter:
        # Create a block with sorted unique characters
        block = ''.join(sorted(counter, key=sort_key))
        answer.append(block)
        # Subtract the block from the counter
        counter -= Counter(block)
    
    # Join blocks with dashes
    return '-'.join(answer)

