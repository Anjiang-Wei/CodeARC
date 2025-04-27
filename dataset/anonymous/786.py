def solution(phoneNumber):
    import re
    # Check if the phone number matches the required format
    return bool(re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phoneNumber))

