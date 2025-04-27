def solution(customers, n):
    tills = [0] * n
    for customer in customers:
        # Find the till with the minimum time and add the current customer's time
        tills[tills.index(min(tills))] += customer
    # The total time is the maximum time in the tills
    return max(tills)

