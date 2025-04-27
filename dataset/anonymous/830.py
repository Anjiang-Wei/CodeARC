def solution(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0

