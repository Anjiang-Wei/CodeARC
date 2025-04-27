def solution(arr):
    # Create a dictionary mapping numbers to corresponding characters
    d = {str(i): chr(123 - i) for i in range(1, 27)}
    d.update({'27': '!', '28': '?', '29': ' ', '0': ''})
    
    # Convert each number in the array to its corresponding character
    return ''.join(d[str(i)] for i in arr)

