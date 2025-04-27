def solution(version):
    ns = version.split('.')
    i = len(ns) - 1
    while i > 0 and ns[i] == '9':
        ns[i] = '0'
        i -= 1
    ns[i] = str(int(ns[i]) + 1)
    return '.'.join(ns)

