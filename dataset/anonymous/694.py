def solution(s):
    import re
    # Check if the password meets all the criteria using regex
    if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s):
        return 'valid'
    else:
        return 'not valid'

