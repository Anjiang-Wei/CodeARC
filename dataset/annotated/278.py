def insert_asterisks_between_evens(s: str | int | list) -> str:
    import re
    
    # Convert input to string if it's an integer or a list
    if isinstance(s, int):
        s = str(s)
    elif isinstance(s, list):
        s = ''.join(map(str, s))
    
    # Use regex to insert '*' between even digits
    return re.sub(r'(?<=[02468])(?=[02468])', '*', s)

