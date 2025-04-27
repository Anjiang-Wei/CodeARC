def is_convertible_to_float(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False

