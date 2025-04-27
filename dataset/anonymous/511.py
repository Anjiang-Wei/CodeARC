def solution(number, char):
    L = (
        (' #### ', '  ##  ', ' #### ', ' #### ', '##  ##', '######', '   ## ', '######', ' #### ', ' #### ').__getitem__,
        ('##  ##', ' ###  ', '##  ##', '##  ##', '##  ##', '##    ', '  ##  ', '##  ##', '##  ##', '##  ##').__getitem__,
        ('##  ##', '# ##  ', '   ## ', '   ## ', '##  ##', '##### ', ' #### ', '   ## ', ' #### ', '##  ##').__getitem__,
        ('##  ##', '  ##  ', '  ##  ', '   ## ', ' #####', '    ##', '##  ##', '  ##  ', ' #### ', ' #### ').__getitem__,
        ('##  ##', '  ##  ', ' ##   ', '##  ##', '    ##', '    ##', '##  ##', ' ##   ', '##  ##', '  ##  ').__getitem__,
        (' #### ', '######', '######', ' #### ', '    ##', '##### ', ' #### ', ' ##   ', ' #### ', ' ##   ').__getitem__
    )
    
    s1 = char * 40
    s2 = f"{char}{' ' * 38}{char}"
    l = list(map(int, f"{number:05}"))
    
    # Construct the number representation
    result = [s1, s2] + [f"{char}  {' '.join(map(L[i], l))}  {char}" for i in range(6)] + [s2, s1]
    
    # Join the result with newline characters
    return '\n'.join(result)

