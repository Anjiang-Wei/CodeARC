def solution(text, amp, period):
    from math import pi, sin
    
    # Create the sine wave pattern for the text
    result = '\n'.join(
        ' ' * (amp + int(round(sin(i * 2 * pi / period) * amp))) + c 
        for i, c in enumerate(text)
    )
    
    return result

