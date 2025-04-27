def check_attendance_record(s: str) -> bool:
    count = 0
    for i in range(len(s)):
        if s[i] == "A":
            count += 1
            if count == 2:
                return False
        elif i >= 2 and s[i] == "L" and s[i-1] == "L" and s[i-2] == "L":
            return False
    return True

