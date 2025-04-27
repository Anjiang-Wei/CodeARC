def solution(string):
    gl = {
        "a": "α", "b": "β", "d": "δ", "e": "ε", "i": "ι", "k": "κ", "n": "η", "o": "θ",
        "p": "ρ", "r": "π", "t": "τ", "u": "μ", "v": "υ", "w": "ω", "x": "χ", "y": "γ"
    }
    # Convert each letter to its corresponding (L33T+Grεεκ)Case or keep it lowercase
    return "".join([gl.get(letter, letter) for letter in string.lower()])

