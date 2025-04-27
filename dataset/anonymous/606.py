def solution(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

