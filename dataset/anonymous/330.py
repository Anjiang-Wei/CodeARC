def solution(s):
    def is_valid(password):
        # Define criteria for validation
        CRITERIA = (str.islower, str.isupper, str.isdigit)
        # Check if password meets all criteria
        return len(password) > 7 and all(any(map(f, password)) for f in CRITERIA)
    
    return is_valid(s)

