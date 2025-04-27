def character_numericals(s: str) -> str:
    def numericals(s: str) -> str:
        dictio = {}
        t = ""
        for i in s:
            # Increment the count of the character in the dictionary
            dictio[i] = dictio.get(i, 0) + 1
            # Append the count to the result string
            t += str(dictio[i])
        return t
    
    return numericals(s)

