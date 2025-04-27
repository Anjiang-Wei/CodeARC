def solution(people):
    till = {100: 0, 50: 0, 25: 0}

    for paid in people:
        till[paid] += 1
        change = paid - 25
        
        for bill in (50, 25):
            while bill <= change and till[bill] > 0:
                till[bill] -= 1
                change -= bill

        if change != 0:
            return 'NO'
            
    return 'YES'

