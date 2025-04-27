def process_commands(tape: str) -> str:
    ptr, stack, output = 0, [0], []
    
    while ptr < len(tape):
        command = tape[ptr]
        
        if command == '^':
            stack.pop()
        elif command == '!':
            stack.append(0)
        elif command == '+':
            stack[-1] = (stack[-1] + 1) % 256
        elif command == '-':
            stack[-1] = (stack[-1] - 1) % 256
        elif command == '*':
            output.append(chr(stack[-1]))
        elif command == '[' and stack[-1] == 0:
            ptr = tape.find(']', ptr)
        elif command == ']' and stack[-1] != 0:
            ptr = tape.rfind('[', 0, ptr)
        
        ptr += 1
        
    return ''.join(output)

