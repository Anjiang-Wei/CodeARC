def solution(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    budget = startPriceOld
    
    while budget < startPriceNew:
        months += 1
        if months % 2 == 0:
            percentLossByMonth += 0.5
        
        # Decrease the prices of the old and new cars
        startPriceOld *= (100 - percentLossByMonth) / 100
        startPriceNew *= (100 - percentLossByMonth) / 100
        
        # Calculate the total budget available
        budget = savingperMonth * months + startPriceOld
    
    # Return the number of months and the rounded leftover money
    return [months, round(budget - startPriceNew)]

