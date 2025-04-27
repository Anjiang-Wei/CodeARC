def solution(phrase):
    BUTTONS = [
        '1', 'abc2', 'def3',
        'ghi4', 'jkl5', 'mno6',
        'pqrs7', 'tuv8', 'wxyz9',
        '*', ' 0', '#'
    ]
    
    # Calculate the total number of button presses required for the phrase
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)

