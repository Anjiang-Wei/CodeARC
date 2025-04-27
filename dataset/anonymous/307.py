def solution(ver1, ver2):
    # Split the version strings by '.' and convert each part to an integer
    ver1_parts = [int(i) for i in ver1.split(".")]
    ver2_parts = [int(i) for i in ver2.split(".")]
    
    # Compare each part of the version numbers
    for v1, v2 in zip(ver1_parts, ver2_parts):
        if v1 > v2:
            return True
        elif v1 < v2:
            return False
    
    # If all compared parts are equal, compare the length of the version parts
    return len(ver1_parts) >= len(ver2_parts)

