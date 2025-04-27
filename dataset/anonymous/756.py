def solution(txt):
    import re
    
    # Replace dual numbers
    txt = re.sub(r'\b2\s(\S+)s', r'2 bu\1', txt)
    
    # Replace paucal numbers
    txt = re.sub(r'\b([3-9])\s(\S+)s', r'\1 \2zo', txt)
    
    # Replace plural numbers
    txt = re.sub(r'(\d{2,})\s(\S+)s', r'\1 ga\2ga', txt)
    
    return txt

