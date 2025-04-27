def find_mating_pairs(required_pairs: int, input_string: str) -> [str, bool]:
    import re
    # Find all mating pairs using regex
    pairs = re.findall(r"B8|8B", input_string)
    # Join pairs into a single string and check if the count is sufficient
    return ["".join(pairs), len(pairs) >= required_pairs]

