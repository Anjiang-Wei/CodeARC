def generate_sequence(signature: list, n: int) -> list:
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output

