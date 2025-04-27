def solution(message, code):
    diffs = "".join(str(c - ord(m) + 96) for c, m in zip(code, message))
    
    for size in range(1, len(code) + 1):
        key = diffs[:size]
        # Check if repeating the key matches the diffs
        if (key * len(code))[:len(code)] == diffs:
            return int(key)

