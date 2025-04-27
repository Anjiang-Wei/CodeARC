def sort_and_reconstruct(xs: list[int]) -> list[int]:
    es = sorted(x for x in xs if x % 2 == 0)  # Sort even numbers in ascending order
    os = sorted((x for x in xs if x % 2 != 0), reverse=True)  # Sort odd numbers in descending order
    return [(es if x % 2 == 0 else os).pop() for x in xs]  # Reconstruct the array with sorted values

