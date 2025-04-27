def solution(code, tape):
    tape = list(map(int, tape))
    ptr = step = loop = 0
    
    while 0 <= ptr < len(tape) and step < len(code):
        command = code[step]
        
        if loop:
            if command == "[": 
                loop += 1
            elif command == "]": 
                loop -= 1
        
        elif command == ">": 
            ptr += 1
        elif command == "<": 
            ptr -= 1
        elif command == "*": 
            tape[ptr] ^= 1        
        elif command == "[" and tape[ptr] == 0: 
            loop += 1
        elif command == "]" and tape[ptr] == 1: 
            loop -= 1
    
        step += 1 if not loop else loop // abs(loop)
    
    return "".join(map(str, tape))

