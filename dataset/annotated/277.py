def is_single_edit_palindrome(s: str) -> bool:
    v = sum(s[i] != s[-1-i] for i in range(len(s) // 2))
    # Check if there is exactly one mismatch or if the string is already a palindrome with an odd length
    return v == 1 or (v == 0 and len(s) % 2 == 1)

