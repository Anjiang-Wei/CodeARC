from typing import List

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    p = flowerbed.count(1)
    m = len(flowerbed) // 2
    if p + n <= m + 1:
        pos = 0
        while pos < len(flowerbed):
            if n == 0:
                return True
            if pos + 1 < len(flowerbed):
                if flowerbed[pos] == 0 and flowerbed[pos + 1] == 0:
                    n -= 1
                    pos += 2
                elif flowerbed[pos] == 1:
                    pos += 2
                else:
                    pos += 3
            else:
                if flowerbed[pos] == 0:
                    n -= 1
                    pos += 2
        return n == 0
    else:
        return False

