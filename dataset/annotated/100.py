from typing import List, Any

def filter_out_elements(source_list: List[Any], exclusion_list: List[Any]) -> List[Any]:
    return [x for x in source_list if x not in exclusion_list]

