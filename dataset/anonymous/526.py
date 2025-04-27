def solution(s):
    from os.path import commonprefix
    
    # Calculate the sum of similarities of the string with each of its suffixes
    return sum(len(commonprefix([s, s[i:]])) for i in range(len(s)))

