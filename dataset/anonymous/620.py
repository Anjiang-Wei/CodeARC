def solution(h):
    st = []
    m = 0
    i = 0
    while i < len(h):
        if len(st) == 0 or h[st[-1]] <= h[i]:
            st.append(i)
            i += 1
        else:
            l = st.pop()
            m = max(m, h[l] * (i if len(st) == 0 else i - st[-1] - 1))
    while len(st) > 0:
        l = st.pop()
        m = max(m, h[l] * (i if len(st) == 0 else i - st[-1] - 1))
    return m

