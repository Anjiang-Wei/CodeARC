def solution(l, w, h):
    from math import ceil

    numbers = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"
    }

    # Calculate the total area to be covered
    area = 2 * (l + w) * h

    # Calculate the number of rolls needed, considering the extra 15%
    rolls_needed = ceil(area * 1.15 / 5.2)

    # Return the number of rolls as a word
    return "zero" if l * w == 0 else numbers[rolls_needed]

