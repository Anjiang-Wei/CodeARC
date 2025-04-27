def solution(num, s):
    if not (isinstance(num, int) and isinstance(s, int)) or num < 0 or s < 0:
        return "Not valid"
    
    ans, num = [], max(num, 11)
    
    # Loop until we find 's' palindromes
    while len(ans) != s:
        # Check if the number is a palindrome
        if num == int(str(num)[::-1]):
            ans.append(num)
        num += 1
    
    return ans

