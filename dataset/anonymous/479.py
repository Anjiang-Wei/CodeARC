def solution(s):
    # Count lowercase and uppercase letters
    lower_count = sum(1 for i in s if i.islower())
    upper_count = sum(1 for i in s if i.isupper())
    
    # Return the string in lower or upper case based on the counts
    return s.lower() if lower_count > upper_count else s.upper()

