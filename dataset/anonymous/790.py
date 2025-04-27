def solution(s):
    results = []
    
    for letter in s:
        # Get binary representation of ASCII value, excluding '0b' prefix
        dec_repr = bin(ord(letter))[2:]
        # Check if there are more zeros than ones and if the letter is not already in results
        if (dec_repr.count("0") > dec_repr.count("1")) and (letter not in results):
            results.append(letter)
    
    return results

