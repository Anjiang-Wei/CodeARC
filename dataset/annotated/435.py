def process_tape(tape: str) -> str:
    memory, ptr, output, iCmd = {}, 0, "", 0
    
    while True:
        cmd = tape[iCmd]
        if   cmd == ">":  ptr += 1
        elif cmd == "<":  ptr -= 1
        elif cmd == "+":  memory[ptr] = (memory.get(ptr, 0) + 1) % 256
        elif cmd == "-":  memory[ptr] = (memory.get(ptr, 0) - 1) % 256
        elif cmd == "*":  output += chr(memory.get(ptr, 0))
        elif cmd == "&":  break
        elif cmd == "/":  iCmd += memory.get(ptr, 0) == 0
        elif cmd == "\\": iCmd += memory.get(ptr, 0) != 0
        iCmd = (iCmd+1) % len(tape)
    
    return output

