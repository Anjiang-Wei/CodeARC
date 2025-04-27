def create_sine_wave_pattern(text: str, amp: int, period: int) -> str:
    from math import pi, sin
    
    # Create the sine wave pattern for the text
    result = '\n'.join(
        ' ' * (amp + int(round(sin(i * 2 * pi / period) * amp))) + c 
        for i, c in enumerate(text)
    )
    
    return result

