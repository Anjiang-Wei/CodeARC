def sort_odds_keeping_evens(arr: list[int]) -> list[int]:
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    # Create a new list where even numbers remain in place and odd numbers are sorted
    return [x if x % 2 == 0 else odds.pop() for x in arr]

