from typing import List

def decompress_rle_image(
    height: int, 
    width: int, 
    compressed: List[int]
) -> List[List[int]]:
    res, left, i, color = [], 0, 0, 0
    
    for h in range(height):
        tot, tmp = 0, []
        
        # If starting with white, add 0 for black
        if color == 1:
            tmp.append(0)
        
        while tot < width and i < len(compressed):
            if left:
                if left <= width - tot:
                    tmp.append(left)
                    tot, left, color = tot + left, 0, 1 - color
                else:
                    tmp.append(width - tot)
                    left -= width - tot
                    tot = width
            else:
                val = compressed[i]
                i += 1
                if tot + val <= width:
                    tmp.append(val)
                    tot, color = tot + val, 1 - color
                else:
                    tmp.append(width - tot)
                    left = val - (width - tot)
                    tot = width
        
        # Ensure even length by appending 0 or remaining left
        if len(tmp) % 2:
            tmp.append(left if h == height - 1 else 0)
        
        res.append(tmp)
    
    return res

