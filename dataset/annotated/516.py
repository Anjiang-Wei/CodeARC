from typing import List, Tuple

def filter_users_with_suffix(logins: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    return list(filter(lambda a: a[0].endswith('_'), logins))

