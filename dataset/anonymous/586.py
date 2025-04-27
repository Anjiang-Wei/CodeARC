def solution(rt):
    return {
        d: rt[d] if d in rt
        else (rt["a"]**2 + rt["b"]**2)**0.5 if d == "c"
        else (rt["c"]**2 - rt[(set("ab") - {d}).pop()]**2)**0.5
        for d in "abc"
    }

