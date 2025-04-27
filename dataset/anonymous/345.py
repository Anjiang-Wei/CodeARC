def solution(num):
    if type(num) != int or num < 0:
        return "Not valid"
    
    s = str(num)
    
    # Check for palindromes of length 2 or 3
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2]:
            return True
    
    # Check for palindromes of length 2 at the end
    return len(s) != 1 and s[-1] == s[-2]

