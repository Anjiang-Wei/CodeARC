import re

def reformat_date_to_dd_mm_yyyy(dt: str) -> str:
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', r'\3-\2-\1', dt)

