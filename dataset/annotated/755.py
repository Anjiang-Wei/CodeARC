def calculate_custom_hash(s: str) -> int:
    a = sum(ord(c) for c in s)
    b = sum(ord(b) - ord(a) for a, b in zip(s, s[1:]))
    c = (a | b) & (~a << 2)
    # Calculate the hash value
    d = c ^ (32 * (s.count(" ") + 1))
    return d

