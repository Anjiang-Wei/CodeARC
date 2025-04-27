from typing import Any, List

def get_item_with_default(items: List[Any], index: int, default_value: Any) -> Any:
    try:
        return items[index]
    except IndexError:
        return default_value

