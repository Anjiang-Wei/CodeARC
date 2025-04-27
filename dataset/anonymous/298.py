def solution(data):
    if not data.isdigit():
        return ''
    
    result = []
    count = 1
    last = data[0]
    
    for char in data[1:]:
        if char == last:
            count += 1
        else:
            result.append(str(count) + last)
            last = char
            count = 1
    
    result.append(str(count) + last)
    
    return ''.join(result)

