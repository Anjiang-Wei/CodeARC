def execute_custom_tape(tape: str) -> str:
    memory, ptr, output = {0: 0}, 0, ""
    
    for command in tape:
        if command == ">":
            ptr += 1
        elif command == "<":
            ptr -= 1
        elif command == "!":
            memory[len(memory)] = 0
        elif command == "*":
            output += chr(memory.get(ptr, 0) % 256)
        elif ptr in memory:
            if command == "+":
                memory[ptr] += 1
            elif command == "-":
                memory[ptr] -= 1
            elif command == "/":
                memory[ptr] = 0
    
    return output

