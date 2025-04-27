def solution(stg=None, binary=None, mode='encode'):
    if mode == 'encode' and stg is not None:
        # Convert each character to its ASCII value, then to an 8-bit binary string
        # Replace each '0' with '000' and each '1' with '111'
        return "".join(digit * 3 for char in stg for digit in f"{ord(char):08b}")
    
    elif mode == 'decode' and binary is not None:
        # Split the binary string into chunks of 3 and determine the most common bit
        def chunks(seq, size):
            return (seq[i:i+size] for i in range(0, len(seq), size))
        
        def get_digit(triplet):
            return max(triplet, key=triplet.count)
        
        def get_char(byte):
            return chr(int(byte, 2))
        
        reduced = (get_digit(triplet) for triplet in chunks(binary, 3))
        # Convert the reduced binary string back to characters
        return "".join(get_char(byte) for byte in chunks("".join(reduced), 8))
    
    else:
        raise ValueError("Invalid mode or input")

