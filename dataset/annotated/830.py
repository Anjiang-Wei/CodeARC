def max_frequency(collection: list) -> int:
    if collection:
        return max([collection.count(item) for item in collection])
    return 0

