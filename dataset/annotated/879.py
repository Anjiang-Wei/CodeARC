def convert_spreadsheet_notation(s: str) -> str:
    import re

    nums = re.findall(r'(\d+)', s)
    if len(nums) == 2:
        n, cStr = int(nums[1]), ''
        while n:
            n, r = divmod(n-1, 26)
            cStr += chr(r + 65)
        # Convert from RnCn to spreadsheet format
        return "{}{}".format(cStr[::-1], nums[0])
    else:
        # Convert from spreadsheet format to RnCn
        return "R{}C{}".format(nums[0], sum(26**i * (ord(c)-64) for i, c in enumerate(re.sub(r'\d', '', s)[::-1])))

