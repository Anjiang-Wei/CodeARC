def generate_ascii_tree(chars: str, n: int) -> str:
    from itertools import cycle
    
    # Create an iterator that cycles through the characters
    it = cycle(chars)
    
    # Build the leaves of the tree
    tree = [
        ' '.join(next(it) for _ in range(i)).center(2 * n).rstrip()
        for i in range(1, n + 1)
    ]
    
    # Add the trunk of the tree
    tree.extend(
        '|'.center(2 * n).rstrip()
        for _ in range(n // 3)
    )
    
    # Join the tree parts into a single string with new lines
    return '\n'.join(tree)

