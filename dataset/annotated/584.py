def assess_carpet_risk(x: int, y: str) -> str:
    # Calculate the sum of ASCII values and alphabetical positions
    total = sum(ord(e) - 96 * (i % 2 != 0) for i, e in enumerate(y))
    
    # Determine if the carpet catches fire
    return 'Fire!' if x != 0 and x * 0.7 < total else 'That was close!'

