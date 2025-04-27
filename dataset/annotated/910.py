def is_vampire_number(candidate: int, fang1: int) -> bool:
    # Convert the product and fangs to strings, sort them, and compare
    return sorted(str(candidate * fang1)) == sorted(str(candidate) + str(fang1))

