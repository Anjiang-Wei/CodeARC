def morse_to_integer(s: str) -> int:
    MORSE_TO_NUM = {
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
    }
    # Convert each 5-character Morse code segment to a number
    return int("".join(MORSE_TO_NUM[s[i:i+5]] for i in range(0, len(s), 5)))

