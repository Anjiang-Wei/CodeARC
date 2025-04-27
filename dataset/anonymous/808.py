def solution(d):
    class CustomDict(dict):
        def __getitem__(self, pk):
            # Find the minimum key that starts with the given prefix
            k = min((k for k in self if k.startswith(pk)), default=None)
            # Return the value for the found key or None if no key is found
            return k if k is None else super().__getitem__(k)

    return CustomDict(d)

