def solution(l):
    snapshots = []
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                snapshots.append(l[:])  # Capture the snapshot after each swap
    return snapshots

