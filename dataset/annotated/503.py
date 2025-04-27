def decode_cipher(cipher: str) -> str:
    out = ""
    while cipher:
        # Determine the length of the ASCII code: 2 for '9x', 3 otherwise
        l = 2 if cipher[0] == "9" else 3
        # Convert the ASCII code to a character and append to output
        out += chr(int(cipher[:l]))
        # Remove the processed part from the cipher
        cipher = cipher[l:]
    return out

