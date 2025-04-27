from collections import Counter
from typing import List, Dict, Any

def count_frequencies(elements: List[Any]) -> Dict[Any, int]:
    freq_count = Counter(elements)
    return freq_count

