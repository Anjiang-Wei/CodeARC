def solution(strings):
    head0, tail0 = strings[0].split(':')
    head1, tail1 = strings[1].split(':')
    return [head0 + ':' + tail1, head1 + ':' + tail0]

