import heapq as hq

def solution(iterable):
    hq.heapify(iterable)
    return [hq.heappop(iterable) for _ in range(len(iterable))]

