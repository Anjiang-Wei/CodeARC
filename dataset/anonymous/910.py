def solution(x, y):
    # Convert the product and fangs to strings, sort them, and compare
    return sorted(str(x * y)) == sorted(str(x) + str(y))

