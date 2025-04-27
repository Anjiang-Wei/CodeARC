def can_form_palindrome_grid(letters: str) -> bool:
    from collections import Counter
    
    n = int(len(letters)**0.5)
    
    # Check if the length of the string is a perfect square
    if n * n != len(letters):
        return False
    
    # Count the frequency of each letter
    letter_counts = Counter(letters)
    
    # Check if the number of letters with odd frequency is less than or equal to n
    odd_count = sum(count % 2 for count in letter_counts.values())
    
    return odd_count <= n

