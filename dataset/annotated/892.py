def are_in_love(flower1: int, flower2: int) -> bool:
    # If the sum of petals is odd, they are in love (return True), otherwise not (return False)
    return (flower1 + flower2) % 2 == 1

