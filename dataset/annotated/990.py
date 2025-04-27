def find_palindromes(start_num: int, count: int) -> list[int]:
    if not (isinstance(start_num, int) and isinstance(count, int)) or start_num < 0 or count < 0:
        return "Not valid"
    
    ans, start_num = [], max(start_num, 11)
    
    # Loop until we find 'count' palindromes
    while len(ans) != count:
        # Check if the number is a palindrome
        if start_num == int(str(start_num)[::-1]):
            ans.append(start_num)
        start_num += 1
    
    return ans

