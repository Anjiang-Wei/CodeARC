def longest_palindromic_substring_length(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    maxPal, tmpPal = 0, 1
    count_dct = {}
    inPal = False
    
    for i, l in enumerate(s):
        count_dct[l] = count_dct.get(l, 0) + 1
        
        if not inPal and count_dct[l] >= 2:
            if l == s[i-1]:
                inPal = True
                tmpPal = 2
            elif l == s[i-2]:
                inPal = True
                tmpPal = 3
        elif inPal and l == s[max(0, i-tmpPal-1)]:
            tmpPal += 2
        else:
            inPal = False
            tmpPal = 1
        
        maxPal = max(maxPal, tmpPal)
    
    return maxPal

